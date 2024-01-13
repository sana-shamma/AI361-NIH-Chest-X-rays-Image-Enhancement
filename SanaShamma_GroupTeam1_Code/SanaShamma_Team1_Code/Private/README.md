# Image Processing Competition 🩻

## Image Tonemapping and Grouping 💡

This code performs tonemapping on chest x-rays images and groups them based on custom brightness ranges. The tonemapping is done using Drago's method with group-specific parameters, and the grouped images are saved in separate folders. The goal is enhancing the quality of the images.

## Requirements 📋

Make sure you have the following Python libraries installed:
- Python 3
- OpenCV (`cv2`)
- NumPy (`numpy`)

## Installation 🛠
1. Install Python: [Python Downloads](https://www.python.org/downloads/)
2. Install required packages:

    ```
    pip install opencv-python numpy
    ```

## Configuration 🔧

1. In the input_folder variable, put the path to your input images folder.
2. At the current level, create a folder called (`grouping`). Inside it, create another folder called (`output`), and within that, create a subfolder called (`Final`).
3. In the output_folder variable, put the path to the (`output`) folder that you have just created.

## Usage ▶️
Run the script using the following command:
   
```
python file_name.py
```

## Folder Structure 📂
The output folder will have the following structure:

grouping/output/  
|  
├── group1/  
│   ├── 1.png  
│   ├── 2.png  
│   └── ...  
│  
├── group2/  
│   ├── 3.png  
│   ├── 4.png  
│   └── ...  
│  
├── ...  
│  
└── final/  
    ├── 1.png  
    ├── 2.png  
    ├── 3.png  
    ├── 4.png  
    └── ...  

## Output 🚀

The grouped and tonemapped images will be saved in subfolders within the specified output folder. The folder structure will be as follows:

- `group1/`: Images belonging to Group 1
- `group2/`: Images belonging to Group 2
- ...
- `Final/`: All images, regardless of their group.

## Authors ✍️

- Salwa Shamma - 4010405
- Samah Shamma - 4010403
- Sana Shamma - 4010404

