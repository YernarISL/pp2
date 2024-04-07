import pygame
import math
from sys import exit

pygame.init()

#color palette
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
colors = [white, black, red, green, blue, yellow]
colorID = 1
brushAndEraser = [3, 50]
brushID = 0

screen = pygame.display.set_mode((1280, 720))
rectLayer = pygame.Surface((1280, 720))
screen.fill(white)
rectLayer.fill(white)
running = True
clock = pygame.time.Clock()

prevpos = (0, 0)
currpos = (0, 0)

LMBpressed = False
RMBpressed = False
MBpressed = False

def createRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def createCircle(x1, y1, x2, y2):
    radius = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) 
    return radius
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevpos = event.pos
        if event.type == pygame.MOUSEMOTION:
            currpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            RMBpressed = True
            prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            RMBpressed = False
            rectLayer.blit(screen, (0, 0))  
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            MBpressed = True
            prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            MBpressed = False
            rectLayer.blit(screen, (0, 0))  
    if LMBpressed:
        pygame.draw.line(screen, colors[colorID], prevpos, currpos, brushAndEraser[brushID])
        pygame.draw.line(rectLayer, colors[colorID], prevpos, currpos, brushAndEraser[brushID])
    if RMBpressed:
        screen.blit(rectLayer, (0, 0))
        pygame.draw.rect(screen, colors[colorID], createRect(prevpos[0], prevpos[1], currpos[0], currpos[1]), 3)
    if MBpressed:
        screen.blit(rectLayer, (0, 0))
        pygame.draw.circle(screen, colors[colorID], prevpos, createCircle(prevpos[0], prevpos[1], currpos[0], currpos[1]), 3)
    key = pygame.key.get_pressed()     
    if key[pygame.K_r]:
        colorID = 2
        brushID = 0
    if key[pygame.K_l]:
        colorID = 4
        brushID = 0
    if key[pygame.K_b]:
        colorID = 1
        brushID = 0
    if key[pygame.K_g]:
        colorID = 3
        brushID = 0
    if key[pygame.K_0]:
        colorID = 0
        brushID = 1
    if key[pygame.K_y]:
        colorID = 5
        brushID = 0  
    if not RMBpressed and not MBpressed:
        prevpos = currpos

    pygame.display.update()
    clock.tick(60)