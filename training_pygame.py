import pygame as pg
from pygame.locals import *

# Каркас игры на Pygame
pg.display.set_mode((600,400))

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
