# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys

FPS = 10
GREEN_COLOR = [0, 128, 0]
LIME_COLOR = [0,255,0]
RED_COLOR = [255,0,0]
BLUE_COLOR = [0,0,255]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600,400))

screen.fill(GREEN_COLOR)

pygame.display.update()

map = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

while True:

    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill(GREEN_COLOR)
    pygame.draw.rect(screen, LIME_COLOR, (0,0,20,20))
    pygame.draw.rect(screen, RED_COLOR, (20,0,20,20))
    pygame.draw.rect(screen, BLUE_COLOR, (40,0,20,20))

    pygame.display.update()