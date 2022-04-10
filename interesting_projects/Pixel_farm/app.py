import pygame
import sys

pygame.init()

SIZE = (100, 100)

class PixelFarm:
    def __init__(self):
        pygame.display.set_caption('Pixel Farm')

        self.screen = pygame.display.set_mode(SIZE)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    app = PixelFarm()
    app.run()