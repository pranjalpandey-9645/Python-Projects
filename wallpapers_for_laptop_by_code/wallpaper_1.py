from PIL import Image, ImageDraw

img = Image.new("RGB", (1920, 1080), color="black")
draw = ImageDraw.Draw(img)

# Example: glowing circle (aura effect)
for r in range(100, 0, -10):
    draw.ellipse((860 - r, 440 - r, 1060 + r, 640 + r), fill=(r * 2, r * 2, r * 2))

# Example: dark warrior silhouette (simple version)
draw.rectangle((920, 480, 1000, 800), fill="gray")

img.save("generated_wallpaper.png")
