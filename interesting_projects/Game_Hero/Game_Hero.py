# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys

FPS = 60
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_mode((600,400))

pygame.display.update()

map = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

while True:

    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()