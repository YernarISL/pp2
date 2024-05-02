import pygame
import psycopg2
from sys import exit
from random import randint
pygame.init()

screen = pygame.display.set_mode((600, 600))
white = (255, 255, 255)


WIDTH = 600
HEIGHT = 600

# Colors
wall_color = (87, 151, 85)
panel_color = (69, 118, 68)
ligth_green = (130, 218, 128)
dark_green = (125, 206, 123)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(wall_color)
score_panel = pygame.Surface((WIDTH, 60))
score_panel.fill(panel_color)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
FPS = 5

cell = 30

def execute():
    create_grid()
    screen.blit(score_panel, (0, 0))
    snake.draw()
    snake.move()
    snake.collision()
    food.collide()
    food.draw()

def create_grid():
    cell_colors = [ligth_green, dark_green]
    for i in range(3, (HEIGHT - 20) // cell):
        for j in range(1, (WIDTH - 20) // cell):
            cell_rect = pygame.Rect(j * cell, i * cell, cell, cell)
            pygame.draw.rect(screen, cell_colors[(i + j) % 2], cell_rect)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 0
        self.dy = -1
        self.over = False
    def draw(self):
        self.head = self.body[0]
        pygame.draw.rect(screen, (0, 100, 255), (self.head.x * cell, self.head.y * cell, cell, cell))

        for segment in self.body[1:]:
            pygame.draw.rect(screen, (0, 150, 255), (segment.x * cell, segment.y * cell, cell, cell))
        
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def collision(self):
        if self.head.x == food.pos.x and self.head.y == food.pos.y:
            self.body.append(Point(self.head.x, self.head.y))

        if self.head.x >= 20:
            self.over = True
            exit()
        if self.head.x < 0:
            self.over = True
            exit()
        if self.head.y >= 20:
            self.over = True
            exit()
        if self.head.y < 2:
            self.over = True
            exit()

class Food:
    def __init__(self):
        self.pos = Point(randint(3, WIDTH // cell - 3), randint(4, WIDTH // cell - 4))
        self.count = 0  
        self.level = 0

    def collide(self):
        head = snake.body[0]
        if self.pos.x == head.x and self.pos.y == head.y:
            self.pos = Point(randint(3, WIDTH // cell - 3), randint(4, WIDTH // cell - 4))  
            self.count += 1

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.pos.x * cell, self.pos.y * cell, cell, cell))

snake = Snake()
food = Food()


def counting():
    if food.count % 5 == 0 and food.count != 0:
        food.level = food.count // 5

def Game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        execute()
        counting()
        pygame.display.update()
        clock.tick(FPS)


conn = psycopg2.connect(
            host='localhost',
            dbname='Snake',
            user='postgres',
            password='Ernar03092005'
        )
cur = conn.cursor()
cur.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
            Player VARCHAR(255),
            Level INT,
            Score INT
            )
            """
        )
conn.commit()

def insert_data():
    cur.execute(
       f"""
        INSERT INTO Users (Player, Level, Score) VALUES (
        '{menu.user_text}', {food.level}, {food.count}
        )
        """
    )
    conn.commit()

class Menu:
    def __init__(self):
        self.background = pygame.image.load('assets\\back.png')
        self.user_font = pygame.font.Font('assets\\font.ttf', 30)
        self.content_font = pygame.font.Font('assets\\font.ttf', 40)
        self.title_font = pygame.font.Font('assets\\font.ttf', 50)
        self.user_text = ''
        self.play_font = pygame.font.Font('assets\\font.ttf', 40) 
        self.running = True
        self.play_status = False

    def interface(self):
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            self.player_text_surface = self.content_font.render("Player:", True, white)
            self.snake_text_surface = self.title_font.render("Snake", True, white)
            self.user_text_surface = self.user_font.render(self.user_text, True, white)
            self.level_text_surface = self.content_font.render("Level:", True, white)
            self.score_text_surface = self.content_font.render("Score:", True, white)
            self.play_font_surface = self.title_font.render("PLAY", True, white)

            self.play_rect = self.play_font_surface.get_rect()
            self.play_rect.topleft = (200, 450)

            if not self.play_status:
                screen.blit(self.background, (0, 0))
            else:
                screen.fill(wall_color)
                Game()
                

            if self.play_rect.collidepoint(mouse_pos) and press[0] == 1:
                self.play_status = True
                print("START")

                
            screen.blit(self.user_text_surface, (360, 185))
            screen.blit(self.snake_text_surface, (180, 40))
            screen.blit(self.player_text_surface, (80, 180))
            screen.blit(self.level_text_surface, (80, 250))
            screen.blit(self.score_text_surface, (80, 320))
            screen.blit(self.play_font_surface, self.play_rect.topleft)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        insert_data()
                    else:
                        self.user_text += event.unicode
                
            pygame.display.update()



menu = Menu()
menu.interface()





