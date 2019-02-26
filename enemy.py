import pygame
from settings import enemy_image
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        raw_surface = pygame.image.load(enemy_image).convert_alpha()
        
        scale_coefficent = ENEMY_SHIP_WIDTH / raw_surface.get_rect().width
        self.image = pygame.transform.rotozoom(
               raw_surface, \
               180,\
               scale_coefficent\
          )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = (WIDTH / 2, 20 )