

import pygame
from settings import player_image
from constants import *

class Player(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          raw_surface = pygame.image.load(player_image).convert_alpha()
          scale_coefficent = PLAYER_SHIP_WIDTH / raw_surface.get_rect().width
          self.image = pygame.transform.rotozoom(
               raw_surface, \
               180,\
               scale_coefficent\
          )

          self.rect = self.image.get_rect()
          self.rect.midbottom = (WIDTH / 2, HEIGHT -20)