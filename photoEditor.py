from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = './editedImgs'

if not os.path.exists(path_out):
    os.makedirs(path_out)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor= 1.5
    enhancher =ImageEnhance.Contrast(edit)
    edit = enhancher.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{path_out}/{clean_name}_edited.png")