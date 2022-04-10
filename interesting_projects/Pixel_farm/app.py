import pygame
import sys
import json
import tkinter as tk
import time

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def timer(n):
    t = time.time()
    while time.time() - t < n:
        pass

class PixelFarm:
    def __init__(self) -> None:
        '''
            Constructor for setting up game
        '''
        
        # Set up title
        pygame.display.set_caption('Pixel Farm')

        # Load settings
        with open('settings.json', 'r') as file:
            self.settings = json.load(file)

        # Set up of screen
        if self.settings["fullscreen"]:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            root = tk.Tk()

            self.screen = pygame.display.set_mode((root.winfo_screenwidth()-100, root.winfo_screenheight()-100))

    def run(self) -> None:
        '''
            Main function of game
        '''

        self.show_start_screen()


        while True:

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.K_q:
                    sys.exit()

            # Fill screen
            self.screen.fill(GREEN)

            # Updating of screen
            pygame.display.update()

    def show_start_screen(self) -> None:
        self.screen.fill(BLACK)
        pygame.display.update()
        timer(5)
        brand_name = pygame.image.load('src/brand_name/1.png')
        self.screen.blit(brand_name, (10, 10))
        pygame.display.update()
        timer(5)





if __name__ == '__main__':
    app = PixelFarm()
    app.run()