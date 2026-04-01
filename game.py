import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((30, 144, 255))  # Dodger blue

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
