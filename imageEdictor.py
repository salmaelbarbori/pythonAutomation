from PIL import Image, ImageEnhance, ImageFilter
import os

path = r"./imgs"
pathOut = r"/imgsIdited"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}.jpg')
