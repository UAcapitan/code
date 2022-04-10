import pygame
import os

pygame.init()

class PixelFarm:
    def __init__(self):
        self.screen = pygame.display.set_mode(100,100)

if __name__ == '__main__':
    app = PixelFarm()