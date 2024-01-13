# Import necessary libraries
import cv2
import os
import numpy as np

# Specify the folder containing the input images
input_folder = "contest-images/contest-images"

# Specify the folder to save the output images
output_folder = "grouping/output"

# Tonemapping parameters
gamma_values = [0.5, 0.48, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
saturation_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bias=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Custom brightness ranges for each group
brightness_ranges = [
    (0.0010191, 0.0015828),
    (0.0015829, 0.0016794),
    (0.0016797, 0.0017575),
    (0.0017576, 0.0018439),
    (0.0018442, 0.0019852),
    (0.0019866, 0.0021062),
    (0.0021072, 0.0023069),
    (0.0023076, 0.0024195),
    (0.0024200, 0.0025142),
    (0.0025147, 0.0029686),
]

# Get an image of all images in the input folder
image_list = os.listdir(input_folder)

# Create subfolders for each group within the output folder
for i in range(1, len(brightness_ranges) + 1):
    group_folder = os.path.join(output_folder, f"group{i}")
    os.makedirs(group_folder, exist_ok=True)

    # Process each image in the input folder
    for image_name in image_list:
        # Check if the file is an image
        if image_name.endswith((".jpg", ".jpeg", ".png")):
            try:
                # Load the image
                image_path = os.path.join(input_folder, image_name)
                original_image = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)
                resized_image = cv2.resize(original_image, (128, 128))

                # Convert the image to the correct format
                # Normalize to the range [0, 1]
                Normalized_image = resized_image.astype('float32') / 65535.0

                # Calculate the mean brightness of the image
                mean_brightness = np.mean(Normalized_image)

                # Determine the group based on custom brightness ranges
                for i, (lower, upper) in enumerate(brightness_ranges):
                    if lower <= mean_brightness <= upper:
                        group_index = i
                        break
                else:
                    group_index = 0

                # Tonemap using Drago's method with group-specific parameters
                tonemap_drago = cv2.createTonemapDrago(
                    gamma = gamma_values [group_index],
                    saturation=saturation_values[group_index],
                    bias=bias [group_index],
                )
                tonemapped_image = tonemap_drago.process(Normalized_image)

                # Convert the image to the correct format for saving
                ldr_image = (tonemapped_image * 255).astype('uint8')

                # Save the image to the output folder
                output_path = os.path.join(output_folder, f"group{group_index + 1}", image_name)
                cv2.imwrite(output_path, ldr_image)
                output_path = os.path.join(output_folder, f"final", image_name)
                cv2.imwrite(output_path, ldr_image)

                print(f"Saved {output_path} (Group {group_index + 1})")

            except Exception as e:
                print(f"Error Processing {image_name}: {str(e)}")

print("Tonemapping and Grouping Completed 🌠")
