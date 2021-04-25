import pygame
import sys

FPS = 60
clock = pygame.time.Clock()

pygame.init()

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