import pygame
from random import randint
from sys import exit
from time import sleep
pygame.init()

screen = pygame.display.set_mode((400, 600))
running = True
clock = pygame.time.Clock()
background = pygame.image.load('Lab8\\images\\AnimatedStreet.png')
n = 0
font = pygame.font.SysFont("Verdana", 60)
font_coin = pygame.font.SysFont("Verdana", 40)
gameover = font.render("Game Over", True, (255, 0, 0))
coins = font_coin.render(str(n), True, (0, 0, 0))
result = font.render(f"Coins: {n}", True, (255, 0, 0))
#Sounds
i = 0
sounds = ['Lab8\\sounds\\background.wav', 'Lab8\\sounds\\crash.wav']
pygame.mixer.music.load(sounds[i])
pygame.mixer.Channel(i).play(pygame.mixer.Sound(sounds[i]))
def playing(i):
    pygame.mixer.music.load(sounds[i])
    pygame.mixer.music.play()
def ring():
    pygame.mixer.music.load('Lab8\\sounds\\smw_coin.wav')
    pygame.mixer.music.play()

class Player(pygame.sprite.Sprite):
    def __init__(self, i):
        self.image = pygame.image.load('Lab8\\images\\Player.png')
        self.image2 = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.move_ip(200, 450)
        self.i = i
    def update(self):
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5 
        if self.key[pygame.K_DOWN] and self.rect.y < screen.get_height() - self.rect.height:
            self.rect.y += 5 
        if self.key[pygame.K_RIGHT] and self.rect.x < screen.get_width() - self.rect.width:
            self.rect.x += 5
        if self.key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5 
        if self.rect.colliderect(enemy.rect):
            pygame.mixer.Channel(i).pause()
            self.i = 1
            playing(self.i) 
            screen.fill((0, 0, 0))
            screen.blit(gameover, (30, 250))
            screen.blit(coin.result, (60, 330))
            pygame.display.update()
            sleep(2)
            exit()
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('Lab8\\images\\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen.get_width() - self.rect.width)
        self.rect.y = 0

    def update(self):
        if self.rect.y < screen.get_height():
            self.rect.y += 7

        if self.rect.y >= screen.get_height():
            self.rect.y = -self.rect.height
            self.rect.x = randint(0, screen.get_width() - self.rect.width)
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Coin(pygame.sprite.Sprite):
    def __init__(self, n, coins, result):
        super().__init__()
        self.image = pygame.image.load('Lab8\\images\\coin1.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen.get_width() - self.rect.width)
        self.rect.y = randint(30, screen.get_height() - self.rect.height)
        self.n = n
        self.coins = coins
        self.result = result
    def update(self):
        if not pygame.sprite.spritecollideany(player, group):
            screen.blit(coin.image, (coin.rect.x, coin.rect.y))
            screen.blit(self.coins, (330, 0))
        else:
            ring()
            self.n += 1
            self.coins = font_coin.render(str(self.n), True, (0, 0, 0))
            screen.blit(self.coins, (330, 0))
            self.result = font.render(f"Coins: {self.n}", True, (255, 0, 0))
            self.rect.x = randint(0, screen.get_width() - self.rect.width)
            self.rect.y = randint(30, screen.get_height() - self.rect.height)
            
player = Player(i)
enemy = Enemy()
coin = Coin(n, coins, result)
group = pygame.sprite.Group()
group.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    
    player.update()
    enemy.update()
    coin.update()
    clock.tick(60)
    pygame.display.flip()