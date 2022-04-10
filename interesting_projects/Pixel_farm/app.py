import pygame
import sys
import json
import tkinter as tk

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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


if __name__ == '__main__':
    app = PixelFarm()
    app.run()