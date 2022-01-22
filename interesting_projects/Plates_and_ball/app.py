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

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Plate(COLORS['white'], 30, 30))
        self.all_sprites.add(Plate(COLORS['black'], SIZE_ROOT['x']-40, 30))

        self.run()

    def run(self):
        while self.work:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.work = False

            keys = pg.key.get_pressed()

            self.all_sprites.update()

            self.bgScreen()
            self.all_sprites.draw(self.root)
            pg.display.flip()

            self.clock.tick(60)


        pg.quit()

    def bgScreen(self):
        self.root.fill(COLORS['black'])
        pg.draw.rect(self.root, COLORS['white'], [SIZE_ROOT['x']/2, 0, SIZE_ROOT['x']/2, SIZE_ROOT['y']])

class Plate(pg.sprite.Sprite):
    def __init__(self, color, x, y):

        super().__init__()

        self.image = pg.Surface((10,50))
        self.image.fill(color)

        pg.draw.rect(self.image, color, [0,0,10,50])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def moveUp(self):
        self.rect.y -= 10

    def moveDown(self):
        self.rect.y += 10

if __name__ == '__main__':
    game = Game()