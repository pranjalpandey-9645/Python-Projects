import pygame
import random
import math
import time

# Initialize
pygame.init()

# Window setup
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lightning Storm Wallpaper")

# Colors
sky_color = (8, 8, 20)
bolt_color = (255, 255, 255)
glow_color = (100, 100, 255)

clock = pygame.time.Clock()

def draw_lightning(surface, x, y, angle, length, thickness, depth):
    if depth == 0 or length < 5:
        return

    rad = math.radians(angle)
    end_x = x + math.cos(rad) * length
    end_y = y + math.sin(rad) * length
    end = (end_x, end_y)

    # Draw glow
    for glow in range(5, 0, -1):
        glow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        glow_surface.set_alpha(20 * glow)
        pygame.draw.line(glow_surface, glow_color, (x, y), end, thickness + glow)
        surface.blit(glow_surface, (0, 0))

    # Draw main bolt
    pygame.draw.line(surface, bolt_color, (x, y), end, thickness)

    # Recurse
    new_angle = angle + random.uniform(-30, 30)
    draw_lightning(surface, end_x, end_y, new_angle, length * 0.8, max(1, thickness - 1), depth - 1)
    if random.random() > 0.7:
        branch_angle = angle + random.uniform(-60, 60)
        draw_lightning(surface, end_x, end_y, branch_angle, length * 0.6, max(1, thickness - 2), depth - 2)

def storm_flash():
    # Draw base dark sky
    screen.fill(sky_color)

    # Random bolts
    for _ in range(random.randint(1, 3)):
        start_x = random.randint(200, 1000)
        draw_lightning(screen, start_x, 0, 90, 150, 3, 6)

    # Screen flash overlay
    flash = pygame.Surface((width, height), pygame.SRCALPHA)
    flash.fill((255, 255, 255, random.randint(30, 60)))  # Semi-transparent white
    screen.blit(flash, (0, 0))

# Main loop
running = True
last_flash_time = 0
flash_interval = random.randint(800, 2000)  # Time between flashes in ms

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_time - last_flash_time > flash_interval:
        storm_flash()
        last_flash_time = current_time
        flash_interval = random.randint(800, 2000)  # Reset interval

    pygame.display.update()
    clock.tick(60)

pygame.quit()
