import pygame 
import datetime

pygame.init()
screen = pygame.display.set_mode((700, 525))
running = True
clock = pygame.time.Clock()

minutes = datetime.datetime.now().minute
seconds = datetime.datetime.now().second
secondsArrow = -seconds * 6
minutesArrow = -minutes * 6 - 50

mickeyclock = pygame.image.load('Lab7\\images\\clock.png')
scaledClock = pygame.transform.scale(mickeyclock, (700, 525))
right = pygame.image.load('Lab7\\images\\right.png')
left = pygame.image.load('Lab7\\images\\left.png')
scaledRight = pygame.transform.scale(right, (right.get_width() // 2, right.get_height() // 2))
scaledLeft = pygame.transform.scale(left, (left.get_width() // 2, left.get_height() // 2))

img_rect_right = scaledRight.get_rect(x = 0, y = 0)
img_rect_left = scaledLeft.get_rect(x = 340, y = 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    rotationRight = pygame.transform.rotate(scaledRight, minutesArrow)
    rotationLeft = pygame.transform.rotate(scaledLeft, secondsArrow)
    rotated_rect_right =  rotationRight.get_rect()
    rotated_rect_right.center = img_rect_right.center
    rotated_rect_left = rotationLeft.get_rect()
    rotated_rect_left.center = img_rect_left.center

    screen.blit(scaledClock, (0, 0))
    screen.blit(rotationLeft, rotated_rect_left)
    screen.blit(rotationRight, rotated_rect_right)
    secondsArrow -= 6
    if datetime.datetime.now().second == 59:
        minutesArrow -= 6
    clock.tick(1)
    pygame.display.flip()