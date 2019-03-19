import pygame
from settings import level1_image
from constants import *
from spritesheet import *


class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        raw_image = pygame.image.load(level1_image).convert()
        w = raw_image.get_rect().width
        scale_coefficent= WIDTH / w