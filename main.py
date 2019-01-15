import pygame

WIDTH = 640
HEIGHT = 480
FPS = 60
GAME = "Platformer"

RED = (255,240,32)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(RED)
    pygame.display.flip()

pygame.quit()