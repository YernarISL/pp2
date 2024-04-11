import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rhombus")

# Colors
WHITE = (255, 255, 255)

# Function to calculate the vertices of a rhombus
def rhombus(center, width, height):
    x, y = center
    half_width = width / 2
    half_height = height / 2
    vertices = [(x - half_width, y), (x, y - half_height), (x + half_width, y), (x, y + half_height)]
    return vertices

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

        # Clear the screen
    screen.fill(WHITE)

        # Draw rhombus
    center = (width // 2, height // 2)
    width = 200
    height = 200
    vertices = rhombus(center, width, height)
    pygame.draw.polygon(screen, (0, 0, 0), vertices, 2)

        # Update the display
    pygame.display.flip()

