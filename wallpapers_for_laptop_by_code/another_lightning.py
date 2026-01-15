import pygame
import random
import math

# Initialize pygame
pygame.init()

# Image dimensions
width, height = 1280, 720
screen = pygame.Surface((width, height))

# Colors
dark_sky = (10, 10, 25)
lightning_color = (255, 255, 255)
glow_color = (100, 100, 255)

# Fill background
screen.fill(dark_sky)

def draw_lightning(surface, start_pos, angle, length, thickness, depth):
    if depth == 0 or length < 5:
        return

    rad = math.radians(angle)
    end_x = start_pos[0] + math.cos(rad) * length
    end_y = start_pos[1] + math.sin(rad) * length
    end_pos = (end_x, end_y)

    # Glow layers
    for glow in range(6, 0, -2):
        glow_color_alpha = (*glow_color[:3], int(20 * glow))
        glow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.line(glow_surface, glow_color_alpha, start_pos, end_pos, thickness + glow)
        surface.blit(glow_surface, (0, 0))

    # Main bolt
    pygame.draw.line(surface, lightning_color, start_pos, end_pos, thickness)

    # Recursion
    new_angle = angle + random.uniform(-30, 30)
    draw_lightning(surface, end_pos, new_angle, length * 0.8, max(1, thickness - 1), depth - 1)
    if random.random() > 0.7:
        side_angle = angle + random.uniform(-60, 60)
        draw_lightning(surface, end_pos, side_angle, length * 0.6, max(1, thickness - 2), depth - 2)

# Draw multiple lightning bolts
for _ in range(3):
    start_x = random.randint(300, 1000)
    draw_lightning(screen, (start_x, 0), 90, 150, 3, 7)

# Save output
pygame.image.save(screen, "lightning_wallpaper_advanced.png")
pygame.quit()