# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys

FPS = 60
GREEN_COLOR = [0, 128, 0]
LIME_COLOR = [0,255,0]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600,400))

screen.fill(GREEN_COLOR)

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
    pygame.draw.rect(screen, LIME_COLOR, (0, 0, 20, 20))

    pygame.display.update()