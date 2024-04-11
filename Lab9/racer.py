import pygame
from random import randint
from sys import exit
from time import sleep

pygame.init()

screen = pygame.display.set_mode((400, 600))

running = True
clock = pygame.time.Clock()

background_image = pygame.image.load('Lab8\\images\\AnimatedStreet.png')

n = 0
font = pygame.font.SysFont("Verdana", 60)
font_coin = pygame.font.SysFont("Verdana", 40)
gameover = font.render("Game Over", True, (255, 0, 0))
result = font.render(f"Coins: {n}", True, (255, 0, 0))

#Sounds
background_music = pygame.mixer.Sound('Lab8\\sounds\\background.wav')
pygame.mixer.Channel(1).play(background_music)

def crash():
    crash_sound = pygame.mixer.Sound('Lab8\\sounds\\crash.wav')
    pygame.mixer.Channel(1).play(crash_sound)

def ring():
    ring = pygame.mixer.Sound('Lab8\\sounds\\smw_coin.wav')
    pygame.mixer.Channel(2).play(ring)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('Lab8\\images\\Player.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(200, 450)

    def move(self):
        screen.blit(self.image, (self.rect.topleft))
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5 
        if self.key[pygame.K_DOWN] and self.rect.y < screen.get_height() - self.rect.height:
            self.rect.y += 5 
        if self.key[pygame.K_RIGHT] and self.rect.x < screen.get_width() - self.rect.width:
            self.rect.x += 5
        if self.key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Lab8\\images\\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (randint(0, screen.get_width() - self.rect.width), 0)
        self.speed = 1
        self.max_speed = 15
        self.min_speed = 5

    def move(self):
        self.rect.y += self.min_speed * self.speed

        if self.rect.y >= screen.get_height():
            self.rect.y = -self.rect.height
            self.rect.x = randint(0, screen.get_width() - self.rect.width)
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def collision_check(self):
        if pygame.sprite.spritecollideany(player, enemies):
            crash()
            screen.fill((0, 0, 0))
            screen.blit(gameover, (30, 250))
            screen.blit(coin.result, (60, 330))
            pygame.display.update()
            sleep(3)
            exit()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Lab8\\images\\coin1.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen.get_width() - self.rect.width)
        self.rect.y = randint(30, screen.get_height() - self.rect.height)
        self.size = randint(30, 60)
        self.scaled = pygame.transform.scale(self.image, (self.size, self.size)) 
        self.n = n
        self.result = result
    def draw(self):
        pygame.display.set_caption("Coins: " + str(self.n))
        self.scaled = pygame.transform.scale(self.image, (self.size, self.size))
        screen.blit(self.scaled, (self.rect.x, self.rect.y))
        if pygame.sprite.spritecollideany(player, coins):
            ring()
            self.n += 1
            self.result = font.render(f"Coins: {self.n}", True, (255, 0, 0))
            self.size = randint(30, 60) #This line defines a random coin size
            #We increase the speed until it reaches its maximum
            if enemy.speed * enemy.min_speed <= enemy.max_speed: 
                enemy.speed += 0.1
            self.rect.topleft = (randint(0, screen.get_width() - self.rect.width), randint(0, screen.get_height() - self.rect.height))

player = Player()
enemy = Enemy()
coin = Coin()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(enemy)
coins.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    screen.blit(background_image, (0, 0))

    player.move()
    enemy.move()
    enemy.collision_check()
    coin.draw()
    clock.tick(60)
    pygame.display.update()