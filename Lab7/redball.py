import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))
running = True
clock = pygame.time.Clock()
x = 50
y = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 30:
        y -= 20
    if pressed[pygame.K_DOWN] and y < screen.get_height() - 30:
        y += 20
    if pressed[pygame.K_LEFT] and x > 30:
        x -= 20
    if pressed[pygame.K_RIGHT] and x < screen.get_width() - 30:
        x += 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    clock.tick(60)    
    pygame.display.flip()