# Import necessary libraries
import os
import cv2
import numpy as np

"""
    Calculate the mean pixel value of an image.
    Parameters:
    - image_path: The path to the image file.
    Returns:
    - The mean pixel value of the image.
    Raises:
    - FileNotFoundError: If the specified image file is not found.
"""
def calculate_mean(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert pixel values to float and normalize them
    image = image.astype('float32') / 65535.0

    # Calculate and return the mean of the image pixel values
    return np.mean(image)

"""
    Divide a list of mean values into specified number of groups.
    Parameters:
    - means: A list of mean values.
    - num_groups: The number of groups to divide the mean values into.
    Returns:
    - list: A list of tuples representing the start and end values of each group.
"""
def divide_into_groups(means, num_groups=10):
    # Sort the mean values in ascending order
    sorted_means = np.sort(means)

    # Split the sorted means into 'num_groups' groups
    group_ranges = np.array_split(sorted_means, num_groups)

    # Create a list of tuples representing the start and end values of each group
    return [(group[0], group[-1]) for group in group_ranges]

"""
    Process a folder of images and print the mean value ranges for different groups.
    Parameters:
    - folder_path: The path to the folder containing image files.
    Raises:
    - FileNotFoundError: If the specified folder does not exist.
"""
def main(folder_path):
    # List all files in the specified folder with extensions .png, .jpg, or .jpeg
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Check if there are no image files in the specified folder
    if not image_files:
        print("No image files found in the specified folder.")
        return
    
    # List to store mean values of each image
    means = []
    
    # Calculate mean values for each image in the folder
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        mean_value = calculate_mean(image_path)
        means.append(mean_value)

    # Divide the mean values into groups and get the ranges for each group
    grouped_ranges = divide_into_groups(means)

    # Print the mean value ranges for each group
    for i, (start, end) in enumerate(grouped_ranges):
        print(f"Group {i+1}: Mean Range [{start:.7f}, {end:.7f}]")

# Specify the folder path containing the images
if __name__ == "__main__":
    folder_path = "contest-images/contest-images"

    # Call the main function with the specified folder path
    main(folder_path)
