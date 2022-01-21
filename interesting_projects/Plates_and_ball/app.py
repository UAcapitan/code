import pygame as pg

COLORS = {
    'white': (255,255,255),
    'black': (0,0,0)
}
SIZE_ROOT = {
    'x':700,
    'y':400
}

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Plates and Ball')
        self.root = pg.display.set_mode((SIZE_ROOT['x'],SIZE_ROOT['y']))
        self.clock = pg.time.Clock()
        self.work = True

        self.run()

    def run(self):
        while self.work:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.work = False
            self.clock.tick(60)
            pg.display.flip()

        pg.quit()

    def bg_screen(self):
        self.root.fill(COLORS['black'])
        pg.draw.rect(self.root, COLORS['white'], [SIZE_ROOT['x']/2, 0, SIZE_ROOT['x']/2, SIZE_ROOT['y']])


if __name__ == '__main__':
    game = Game()