import pygame
from sys import exit
from random import randint

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
GameOver = pygame.image.load('images\\gameover.jpg')

running = True
clock = pygame.time.Clock()

CELL = 30
lightGreen = (125, 206, 123)
darkGreen = (118, 192, 116)
 
level = 0
FPS = 5 


def grid():
    colors = [lightGreen, darkGreen]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            cellvalue = pygame.Rect(j * CELL, i * CELL, CELL, CELL)
            pygame.draw.rect(screen, colors[(i + j) % 2], cellvalue)
            
def playing():
    grid()
    snake.move()
    snake.draw()
    snake.check_collision(food)
    food.gen()
    food.draw()
    pygame.display.set_caption("Score: " + str(food.count) + "      Level: " + str(level))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 0
        self.dy = -1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, (0, 156, 255), (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, (246, 235, 26), (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))

        if head.x > WIDTH // CELL - 1:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // CELL
        elif head.y > HEIGHT // CELL - 1:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // CELL
                 
class Food:
    def __init__(self):
        self.pos = Point(randint(0, WIDTH // CELL - 1), randint(0, WIDTH // CELL - 1))
        self.count = 0

    def gen(self):
        head = snake.body[0]
        if self.pos.x == head.x and self.pos.y == head.y:
            self.pos = Point(randint(0, WIDTH // CELL - 1), randint(0, WIDTH // CELL - 1))  
            self.count += 1

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class Stop:
    def __init__(self):
        self.running = running 
        self.btn = pygame.Surface((150, 50))
        self.btn.fill((142, 213, 245))
        self.btn_rect = self.btn.get_rect()
        self.btn_rect.topleft = (230, 350)
        self.font = pygame.font.SysFont('Copperplate Gothic', 40, True)
        self.text = self.font.render("PLAY", True, (0, 0, 0))

    def draw(self):
        screen.blit(self.btn, (self.btn_rect.x, self.btn_rect.y))
        screen.blit(self.text, (235, 350))

    def gameover(self):
        head = snake.body[0]
        for i in range(1, len(snake.body) - 1):
            if head.x == snake.body[i].x and head.y == snake.body[i].y:
                self.running = False
        return self.running
    
    def click(self):
        pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
        if self.btn_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.running = True
        elif key[pygame.K_SPACE]:
            self.running = True
        return self.running

snake = Snake()
food = Food()
restart = Stop()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.body[0].y != snake.body[1].y: 
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.body[0].y != snake.body[1].y:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP and snake.body[0].x != snake.body[1].x:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN and snake.body[0].x != snake.body[1].x:
                snake.dx = 0
                snake.dy = 1

    playing()
    restart.gameover()

    if not restart.running:
        screen.blit(GameOver, (0, 0))
        restart.draw()
        snake.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        food.count = 0
    restart.click()
    pygame.display.update() 
    clock.tick(FPS)