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
     
     def update(self):
          self.speedx = 0
          key_state = pygame.key.get_pressed()
          if(key_state[pygame.K_LEFT]):
               self.speedx = -7
          if (key_state[pygame.K_RIGHT]):
               self.speedx = 7
          self.rect.x += self.speedx     
          if (self.rect.x < 0):
               self.rect.x = 0
          if (self.rect.right > WIDTH):
               self.rect.right = WIDTH   
