# Image Editing Project

This repository contains a Python script to perform batch image editing using the Python Imaging Library (PIL). The script enhances images by applying sharpening, converting to grayscale, and adjusting the contrast.

## Project Structure
- `imgs/` : Directory containing the original images.
- `editedImgs/` : Directory where the edited images will be saved.

## Requirements
- Python 3.x
- PIL (Pillow)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-editing.git
    cd image-editing
    ```

2. Install the required libraries:
    ```sh
    pip install Pillow
    ```

## Usage

1. Place the images you want to edit in the `imgs` directory.

2. Run the script:
    ```sh
    python photoEditor.py
    ```

3. The edited images will be saved in the `editedImgs` directory with the same name as the original images, appended with `_edited`.

## Script Description

```python
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = './editedImgs'

if not os.path.exists(path_out):
    os.makedirs(path_out)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{path_out}/{clean_name}_edited.png")
