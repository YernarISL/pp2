import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
screen.fill((255, 255, 255))
running = True

playing = False
nxt = 0
songs = ['08-Kupla-End-of-the-Road.mp3', 'ambient-piano-logo-165357.mp3', 'angelical-pad-143276.mp3', 'sunflower-street-drumloop-85bpm-163900.mp3']  
pygame.mixer.music.load(f'Lab7\\musics\\{songs[nxt]}')
pygame.mixer.music.play()
pygame.mixer.music.pause()

def nextsong(nxt, songs):
    pygame.mixer.music.load(f'Lab7\\musics\\{songs[nxt]}')
    pygame.mixer.music.play()

# icons
play = pygame.image.load('Lab7\\images\\play2.png')
pause = pygame.image.load('Lab7\\images\\pause.png')
forward = pygame.image.load('Lab7\\images\\fast-forward.png')
backward = pygame.image.load('Lab7\\images\\fast-backward.png')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            playing = not playing
            if playing:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and playing:
            if nxt == len(songs) - 1:
                nxt = 0
                nextsong(nxt, songs)
            else:
                nxt += 1
                nextsong(nxt, songs)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and playing:
            if nxt == 0:
                nxt = len(songs) - 1
                nextsong(nxt, songs)
            else:
                nxt -= 1
                nextsong(nxt, songs)
    if playing:
        screen.blit(pause, (230, 80))
    else:
        screen.blit(play, (230, 80))
    screen.blit(forward, (400, 80))
    screen.blit(backward, (60, 80))
    pygame.display.flip()