from PIL import Image, ImageDraw
import random

width, height = 800, 600
img = Image.new("RGB", (width, height), (10, 10, 30))
draw = ImageDraw.Draw(img)

def draw_lightning(draw, x, y, length, depth):
    if depth == 0 or length < 5:
        return

    end_x = x + random.randint(-20, 20)
    end_y = y + random.randint(20, 40)

    draw.line((x, y, end_x, end_y), fill=(255, 255, 255), width=random.randint(1, 2))

    draw_lightning(draw, end_x, end_y, length * 0.7, depth - 1)
    if random.random() > 0.6:
        draw_lightning(draw, end_x, end_y, length * 0.5, depth - 1)

for _ in range(3):
    start_x = random.randint(300, 500)
    draw_lightning(draw, start_x, 0, 100, 6)

img.save("lightning_wallpaper_pillow.png")
print("Static lightning wallpaper saved as lightning_wallpaper_pillow.png")
