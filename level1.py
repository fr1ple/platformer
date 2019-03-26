import pygame
from settings import level1_image
from constants import *
from spritesheet import *


class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        raw_image = pygame.image.load(level1_image).convert()
        w = raw_image.get_rect().width
        scale_coefficent = WIDTH / w
        self.images = [\
            pygame.transform.rotozoom(raw_image, 0, scale_coefficent),\
            pygame.transform.rotozoom(raw_image, 180, scale_coefficent)\
        ]
        
        h = self.images[0].get_rect().height
        self.block = pygame.Surface((WIDTH,2*h))
       
        self.block.blit(self.images[0], (0, 0))
        self.block.blit(self.images[1], (0, h))

        self.block_height = self.block.get_rect().height

        self.speed = 5
        self.position = HEIGHT - self.block_height

    def update(self):
        self.position1 += self.speed
        self.position2 += self.speed
        if(self.position1 >=HEIGHT):
            self.position1 = self.position2