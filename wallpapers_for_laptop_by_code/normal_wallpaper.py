# Python Pillow: Generative grid with gradient
from PIL import Image, ImageDraw
import random

img = Image.new("RGB", (1920, 1080), "black")
draw = ImageDraw.Draw(img)

for x in range(0, 1920, 20):
    for y in range(0, 1080, 20):
        color = (x % 255, y % 255, (x*y) % 255)
        draw.rectangle([x, y, x+18, y+18], fill=color)

img.save("coded_wallpaper.png")
