from PIL import Image, ImageDraw, ImageFilter
import random
import colorsys

# Setup canvas
width, height = 1920, 1080
bg_color = (5, 5, 10)  # Deep cyber night
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Color palette: Cyberpunk vibes (neon purple, blue, pink, green)
def cyber_color(hue_offset=0):
    hue = (random.random() + hue_offset) % 1.0
    r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(hue, 1, 1)]
    return (r, g, b)

# Generate neon particles (like data sparks)
for _ in range(1500):
    x = random.randint(0, width)
    y = random.randint(0, height)
    radius = random.randint(1, 4)
    glow_color = cyber_color(hue_offset=random.uniform(0.5, 0.9))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=glow_color)

# Add vertical "data streams" (Matrix-style)
for _ in range(120):
    x = random.randint(0, width)
    length = random.randint(100, 600)
    y_start = random.randint(-200, height - length)
    line_color = cyber_color(hue_offset=random.uniform(0.3, 0.7))
    draw.line([(x, y_start), (x, y_start + length)], fill=line_color, width=random.randint(1, 2))

# Apply glow effect
blurred = img.filter(ImageFilter.GaussianBlur(radius=2))
final = Image.blend(img, blurred, alpha=0.5)

# Save & Show
final.save("cyberpunk_particle_wallpaper.png")
final.show()
