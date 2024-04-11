import pygame
import math
from sys import exit

pygame.init()

clock = pygame.time.Clock()

#color palette
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)
gray = (240, 240, 240)

screen = pygame.display.set_mode((1280, 720))
nav_screen = pygame.Surface((1280, 70))
work_screen = pygame.Surface((1280, 720))
screen.fill(white)
work_screen.fill(white)
nav_screen.fill(gray)


running = True

class Palette:
    def __init__(self):
        self.red = pygame.Surface((30, 30))
        self.red_rect = self.red.get_rect()
        self.red_rect.topleft = (600, 20)
        self.red_border = pygame.Surface((32, 32))
        self.red_rect_border = self.red_border.get_rect()
        self.red_rect_border.center = self.red_rect.center
        self.red.fill(red)
        
        self.blue = pygame.Surface((30, 30))
        self.blue_rect = self.blue.get_rect()
        self.blue_rect.topleft = (635, 20)
        self.blue_border = pygame.Surface((32, 32))
        self.blue_rect_border = self.blue_border.get_rect()
        self.blue_rect_border.center = self.blue_rect.center
        self.blue.fill(blue)

        self.green = pygame.Surface((30, 30))
        self.green_rect = self.green.get_rect()
        self.green_rect.topleft = (670, 20)
        self.green_border = pygame.Surface((32, 32))
        self.green_rect_border = self.green_border.get_rect()
        self.green_rect_border.center = self.green_rect.center
        self.green.fill(green)

        self.yellow = pygame.Surface((30, 30))
        self.yellow_rect = self.yellow.get_rect()
        self.yellow_rect.topleft = (705, 20)
        self.yellow_border = pygame.Surface((32, 32))
        self.yellow_rect_border = self.yellow_border.get_rect()
        self.yellow_rect_border.center = self.yellow_rect.center
        self.yellow.fill(yellow)

        self.purple = pygame.Surface((30, 30))
        self.purple_rect = self.purple.get_rect()
        self.purple_rect.topleft = (740, 20)
        self.purple_border = pygame.Surface((32, 32))
        self.purple_rect_border = self.purple_border.get_rect()
        self.purple_rect_border.center = self.purple_rect.center
        self.purple.fill(purple)

        self.orange = pygame.Surface((30, 30))
        self.orange_rect = self.orange.get_rect()
        self.orange_rect.topleft = (775, 20)
        self.orange_border = pygame.Surface((32, 32))
        self.orange_rect_border = self.orange_border.get_rect()
        self.orange_rect_border.center = self.orange_rect.center
        self.orange.fill(orange)

    def output(self):
        nav_screen.blit(self.red, self.red_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.red_rect_border, 2)

        nav_screen.blit(self.blue, self.blue_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.blue_rect_border, 2)

        nav_screen.blit(self.green, self.green_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.green_rect_border, 2)

        nav_screen.blit(self.yellow, self.yellow_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.yellow_rect_border, 2)

        nav_screen.blit(self.orange, self.orange_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.orange_rect_border, 2)

        nav_screen.blit(self.purple, self.purple_rect.topleft)
        pygame.draw.rect(nav_screen, black, self.purple_rect_border, 2)
        

class Selection:
    def __init__(self):
        self.brush_icon = pygame.image.load('Lab9\\images\\brush.png')
        self.triangle_icon = pygame.image.load('Lab9\\images\\traingle.png')
        self.circle_icon = pygame.image.load('Lab9\\images\\circle.png')
        self.rectangle_icon = pygame.image.load('Lab9\\images\\rectangle.png')
        self.right_triangle_icon = pygame.image.load('Lab9\\images\\right-triangle.png')
        self.rhombus_icon = pygame.image.load('Lab9\\images\\rhombus.png')

        self.brush_icon_rect = self.brush_icon.get_rect()
        self.triangle_icon_rect = self.brush_icon.get_rect()
        self.circle_icon_rect = self.circle_icon.get_rect()
        self.rectangle_icon_rect = self.rectangle_icon.get_rect()
        self.right_triangle_icon_rect = self.right_triangle_icon.get_rect()
        self.rhombus_icon_rect = self.rectangle_icon.get_rect()

        self.brush_icon_rect.topleft = (200, 20)
        self.triangle_icon_rect.topleft = (235, 20)
        self.circle_icon_rect.topleft = (270, 20)
        self.rectangle_icon_rect.topleft = (305, 20)
        self.right_triangle_icon_rect.topleft = (340, 20)
        self.rhombus_icon_rect.topleft = (375, 20)
        
        self.choice = ["brush", "rectangle", "circle", "rhombus", "right-triangle", "equilateral-triangle"] 
        self.color_choice = [black, red, green, blue, yellow, orange, purple] 

        self.filling = 2

        self.colorID = 0
        self.shapeID = 0

    def click_to_color(self):
        self.pos = pygame.mouse.get_pos()
        self.press = pygame.mouse.get_pressed()
        if palette.blue_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS BLUE!")
            self.colorID = 3
        elif palette.red_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS RED!")
            self.colorID = 1
        elif palette.green_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS GREEN!")
            self.colorID = 2
        elif palette.yellow_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS YELLOW!")
            self.colorID = 4
        elif palette.orange_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS ORANGE!")
            self.colorID = 5   
        elif palette.purple_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("ITS PURPLE!")
            self.colorID = 6

    def click_to_shape(self):
        self.pos = pygame.mouse.get_pos()
        self.press = pygame.mouse.get_pressed()

        if self.brush_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("BRUSHE")
            self.shapeID = 0
        elif self.rectangle_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("RECTANGLE")
            self.shapeID = 1
        elif self.circle_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("CIRCLE")
            self.shapeID = 2
        elif self.rhombus_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("RHOMBUS")
            self.shapeID = 3
        elif self.right_triangle_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("RIGHT")
            self.shapeID = 4
        elif self.triangle_icon_rect.collidepoint(self.pos) and self.press[0] == 1:
            print("TRSINGLE")
            self.shapeID = 5
    
    def output(self):
        nav_screen.blit(self.brush_icon, self.brush_icon_rect.topleft)
        nav_screen.blit(self.rectangle_icon, self.rectangle_icon_rect.topleft)
        nav_screen.blit(self.triangle_icon, self.triangle_icon_rect.topleft)
        nav_screen.blit(self.circle_icon, self.circle_icon_rect.topleft)
        nav_screen.blit(self.right_triangle_icon, self.right_triangle_icon_rect.topleft)
        # nav_screen.blit(self.rhombus_icon, self.rhombus_icon_rect.topleft)

class Brush:
    def __init__(self):
        self.indicator = option.choice[option.shapeID]
        self.prevpos = (0, 0)
        self.currpos = (0, 0)
        self.LMBpressed = False
        self.color = option.color_choice[option.colorID]

    def draw(self):
        self.indicator = option.choice[option.shapeID]
        self.color = option.color_choice[option.colorID]
        if self.LMBpressed:
            pygame.draw.line(work_screen, self.color, self.prevpos, self.currpos, 2)
        self.prevpos = self.currpos

class Rectangle:
    def __init__(self):
        self.prevpos = (0, 0)
        self.currpos = (0, 0)
        self.LMBpressed = False
        self.color = option.color_choice[option.colorID]
        self.layer = pygame.Surface((1280, 720))
        self.layer.fill(white)

    def create_rect(self, x1, y1, x2, y2):
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
        return self.rect
    
    def draw(self):
        self.color = option.color_choice[option.colorID]
        if self.LMBpressed:
            work_screen.blit(self.layer, (0, 0))
            pygame.draw.rect(work_screen, self.color, self.create_rect(self.prevpos[0], self.prevpos[1], self.currpos[0], self.currpos[1]), 2)

class Circle:
    def __init__(self):
        self.prevpos = (0, 0)
        self.currpos = (0, 0)
        self.LMBpressed = False
        self.color = option.color_choice[option.colorID]

    def calculate_radius(self, x1, y1, x2, y2):
        radius = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) 
        return radius

    def draw(self):
        self.color = option.color_choice[option.colorID]
        if self.LMBpressed:
            work_screen.blit(rectangle.layer, (0, 0))
            pygame.draw.circle(work_screen, self.color, self.currpos, self.calculate_radius(self.prevpos[0], self.prevpos[1], self.currpos[0], self.currpos[1]), 2)

class RightTriangle:
    def __init__(self):
        self.prevpos = (0, 0)
        self.currpos = (0, 0)
        self.LMBpressed = False
        self.color = option.color_choice[option.colorID]

    def draw(self):
        self.color = option.color_choice[option.colorID]
        if self.LMBpressed:
            work_screen.blit(rectangle.layer, (0, 0))
            pygame.draw.polygon(work_screen, self.color, ((self.prevpos[0], self.prevpos[1]), (self.prevpos[0], self.currpos[1]), (self.currpos[0], self.currpos[1])), 2)

class EquilateralTriangle:
    def __init__(self):
        self.prevpos = (0, 0)
        self.currpos = (0, 0)
        self.LMBpressed = False
        self.color = option.color_choice[option.colorID]

    def draw(self):
        self.color = option.color_choice[option.colorID]
        if self.LMBpressed:
            side_l = math.sqrt(pow(self.currpos[0] - self.prevpos[0], 2) + pow(self.currpos[1] - self.prevpos[1], 2))
            height = math.sqrt(3) * side_l / 2
            half_l = side_l / 2
            work_screen.blit(rectangle.layer, (0, 0))
            pygame.draw.polygon(work_screen, self.color, ((self.currpos[0] / 2, self.currpos[1] - height / 2), (self.currpos[0] // 2 - half_l, self.currpos[1] + height / 2), (self.currpos[0] / 2 + half_l, self.currpos[1] + height / 2)), 2)


class Reset:
    def __init__(self):
        self.button = pygame.Surface((90, 40))
        self.button_rect = self.button.get_rect()
        self.button_rect.topleft = (1100, 15)
        self.button.fill((100, 100, 100))
        self.font = pygame.font.SysFont('Verdana', 19, True)
        self.text = self.font.render("RESET", True, white)

    def pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        if self.button_rect.collidepoint(mouse_pos) and press[0] == 1:
            work_screen.fill(white)
            rectangle.layer.fill(white)
            
    def output(self):
        nav_screen.blit(self.button, self.button_rect.topleft)
        nav_screen.blit(self.text, (1110, 20))

palette = Palette()
option = Selection()
brush = Brush()
rectangle = Rectangle()
cicrle = Circle()
r_triangle = RightTriangle()
e_triangle = EquilateralTriangle()
reset = Reset()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        if event.type == pygame.MOUSEMOTION:
            brush.currpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            brush.LMBpressed = True
            brush.prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            brush.LMBpressed = False


        if event.type == pygame.MOUSEMOTION:
            rectangle.currpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            rectangle.LMBpressed = True
            rectangle.prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            rectangle.LMBpressed = False
            rectangle.layer.blit(work_screen, (0, 0))


        if event.type == pygame.MOUSEMOTION:
            cicrle.currpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cicrle.LMBpressed = True
            cicrle.prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            cicrle.LMBpressed = False
            rectangle.layer.blit(work_screen, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            r_triangle.currpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            r_triangle.LMBpressed = True
            r_triangle.prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            r_triangle.LMBpressed = False
            rectangle.layer.blit(work_screen, (0, 0))


        if event.type == pygame.MOUSEMOTION:
            e_triangle.currpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            e_triangle.LMBpressed = True
            e_triangle.prevpos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            e_triangle.LMBpressed = False
            rectangle.layer.blit(work_screen, (0, 0))


    palette.output()
    option.output()
    option.click_to_color()
    option.click_to_shape()
    reset.output()
    reset.pressed()

    if option.choice[option.shapeID] == "brush":
        brush.draw()
    if option.choice[option.shapeID] == "rectangle":
        rectangle.draw()
    if option.choice[option.shapeID] == "circle":
        cicrle.draw()
    if option.choice[option.shapeID] == "right-triangle":
        r_triangle.draw()
    if option.choice[option.shapeID] == "equilateral-triangle":
        e_triangle.draw()

    pygame.draw.line(nav_screen, (180, 180, 180), (0, 70), (1280, 70), 3)
        
    screen.blit(work_screen, (0, 0))
    screen.blit(nav_screen, (0, 0))
    pygame.display.update()

    clock.tick(60)