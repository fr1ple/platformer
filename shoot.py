import pygame
from settings import shoot_image
from spritesheet import Spritesheet
from constants import *


class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(shoot_image)
        self.bullets = ss.images_at([\
            (107, 272, 14, 14), \
            (126, 272, 15, 14), \
            (145, 273, 15, 13), \
            (165, 271, 14, 15), \
            (184, 272, 14, 14), \
            (201, 273, 16 ,14), \
            (221, 273, 15, 13), \
            (240, 271, 14, 15), \
            ], -1)
        self.image = self.bullets[0]
        self.idx = 0
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.speed = 5
        self.frames_count = 0
        self.animate_each_frame = 10

    def update(self):
        self.frames_count += 1
        if (self.frames_count == self.animate_each_frame):
            self.frames_count = 0
            self.idx = 0 if self.idx == (len(self.bullets) -1) else (self.idx + 1)
            self.image = self.bullets[self.idx]

        self.rect.centery -= self.speed

        if (self.rect.midbottom[1] == 0):
            self.kill()