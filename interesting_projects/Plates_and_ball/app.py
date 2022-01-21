import pygame as pg
pg.init()

COLORS = {
    'white': (255,255,255),
    'black': (0,0,0)
}

class Game:
    def __init__(self):
        self.root = pg.display.set_mode(700,500)
        