from PIL import Image, ImageDraw, ImageFilter
import random
import colorsys

# Create canvas
width, height = 1920, 1080
img = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(img)

# Function to get neon-style colors
def get_neon_color(x, y):
    hue = (x * 0.001 + y * 0.0015) % 1.0  # Cycle through hues
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1)]
    return (r, g, b)

# Draw glowing grid
step = 30
for x in range(0, width, step):
    for y in range(0, height, step):
        color = get_neon_color(x, y)
        size = random.randint(16, 26)
        offset = size // 2
        draw.ellipse([x - offset, y - offset, x + offset, y + offset], fill=color)

# Apply a soft glow to simulate neon light
glow = img.filter(ImageFilter.GaussianBlur(radius=3))
final_img = Image.blend(img, glow, alpha=0.6)

# Save and show
final_img.save("neon_grid_wallpaper.png")
final_img.show()
# This code generates a vibrant neon-style wallpaper with a glowing grid effect.
# The colors are derived from the HSV color space to create a dynamic and colorful pattern.