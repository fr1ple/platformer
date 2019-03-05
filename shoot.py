import pygame
from settings import shoot_image
from spritesheet import Spritesheet


class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(shoot_image)
        raw_surface = ss.images_at([(107, 272, 16, 16)], -1)
          
