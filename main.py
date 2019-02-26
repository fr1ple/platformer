import pygame
from  constants import *
from player import Player
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    all_sprites.update()            
                

    screen.fill(RED)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
