import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Best Friends Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)  # Sky color
GROUND = (50, 205, 50)  # Grass color

# Load images
friend1 = pygame.image.load("friend1.png")  # Replace with your character image
friend2 = pygame.image.load("friend2.png")  # Replace with your character image

# Resize images
friend1 = pygame.transform.scale(friend1, (100, 150))
friend2 = pygame.transform.scale(friend2, (100, 150))

# Initial positions
x1, y1 = 100, 400
x2, y2 = 200, 400
speed = 2

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLUE)  # Sky
    pygame.draw.rect(screen, GROUND, (0, 500, WIDTH, 100))  # Ground

    # Move friends smoothly
    x1 += speed
    x2 += speed

    # Loop movement
    if x1 > WIDTH:
        x1 = -100
    if x2 > WIDTH:
        x2 = -100

    # Draw friends
    screen.blit(friend1, (x1, y1))
    screen.blit(friend2, (x2, y2))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()