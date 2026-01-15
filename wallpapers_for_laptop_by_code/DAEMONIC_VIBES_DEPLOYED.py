from PIL import Image, ImageDraw, ImageFont
import random

# Wallpaper size and background
width, height = 1920, 1080
background_color = (10, 10, 10)
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Fonts (adjust the path if needed)
try:
    main_font = ImageFont.truetype("arial.ttf", 120)
    sub_font = ImageFont.truetype("arial.ttf", 24)
except:
    main_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()

# Center position for main label
main_text = "DAEMON"
main_w, main_h = draw.textbbox((0, 0), main_text, font=main_font)[2:]
center_x, center_y = width // 2, height // 2
main_text_pos = (center_x - main_w // 2, center_y - main_h // 2)

# Labels and their colors
labels = [
    ("init.DÆMON();", "cyan"),
    ("System Override: TRUE", "orange"),
    ("Dark Warrior", "violet"),
    ("Ultron-X Interface Ready", "royalblue"),
    ("#DaemonicVibesDeployed", "deeppink"),
    ("Code. Command. Conquer.", "crimson"),
    ("Legion Booting...", "limegreen"),
    ("echo \"Rise of Dæmon\"", "lightgray"),
    ("#DaemonAwakened", "magenta"),
    ("Protocol: SHADOW_WALK", "skyblue"),
    ("Core Override - Alpha", "gold"),
    ("Command Received at 3:00 AM", "lightcoral")
]

# Generate circuit lines
for i, (label, color) in enumerate(labels):
    # Random angle and distance from center
    angle = random.uniform(0, 360)
    length = random.randint(250, 450)
    radians = angle * (3.14159 / 180)
    end_x = int(center_x + length * random.uniform(0.95, 1.1) * random.choice([-1, 1]) * abs(random.random()))
    end_y = int(center_y + length * random.uniform(0.95, 1.1) * random.choice([-1, 1]) * abs(random.random()))

    # Create path segments (angled circuit look)
    mid_x = (center_x + end_x) // 2 + random.randint(-50, 50)
    mid_y = (center_y + end_y) // 2 + random.randint(-50, 50)

    draw.line([(center_x, center_y), (mid_x, mid_y), (end_x, end_y)], fill=color, width=2)
    draw.text((end_x, end_y), label, fill=color, font=sub_font)

# Draw main text at the end (on top of all)
draw.text(main_text_pos, main_text, font=main_font, fill=(0, 255, 255))

# Save output
image.save("daemonic_final_circuit_wallpaper.png")
print("Wallpaper created: daemonic_final_circuit_wallpaper.png")