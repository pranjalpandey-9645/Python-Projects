import ctypes
from PIL import Image, ImageDraw, ImageFont
import os

# === Load your image ===
image_path ="D:/Wallpap/A_digital_painting_in_a_dark_fantasy_art_style_dep.png"
# Ensure the image is a high-resolution warrior-themed wallpaper
# You can replace this with your own warrior-themed image path  
output_path = "warrior_wallpaper_with_text.bmp"

# === Open the image ===
image = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(image)

# === Load a font (change path if needed) ===
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

# === Add your bold, rock-bottom caption ===
caption = "Born from chaos, forged by war, ruled by none."
text_position = (50, image.height - 100)
text_color = (255, 255, 255)  # White

# Shadow for depth
draw.text((text_position[0]+2, text_position[1]+2), caption, font=font, fill=(0, 0, 0))
draw.text(text_position, caption, font=font, fill=text_color)

# === Save as BMP format (required for Windows wallpaper) ===
image.save(output_path, "BMP")

# === Set as wallpaper (Windows only) ===
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(output_path), 3)

print("Wallpaper set with caption! 💀🔥")
