from cmath import rect
import pygame
import sys
import json
import tkinter as tk
import time

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def timer(n):
    t = time.time()
    while time.time() - t < n:
        pass

class ButtonMenu(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))

class Stone(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect(center=(x,y))

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

        root = tk.Tk()

        # Set up of screen
        if self.settings["fullscreen"]:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.screen_size = (root.winfo_screenwidth(), root.winfo_screenheight())
        else:
            self.screen = pygame.display.set_mode((root.winfo_screenwidth()-100, root.winfo_screenheight()-100))
            self.screen_size = (root.winfo_screenwidth()-100, root.winfo_screenheight()-100)

        self.screen_center = (self.screen_size[0]/2, self.screen_size[1]/2)

        self.menu = False

    def run(self) -> None:
        '''
            Main function of game
        '''

        # Start screen showing
        self.show_start_screen()
        self.menu = True
        self.show_menu_screen()
        stone = Stone(BLACK, 20, 30, 50, 60)
        while True:
            # Events
            self.check_events()

            # Fill screen
            self.screen.fill(GREEN)

            self.screen.blit(stone.image, stone.rect)

            # Updating of screen
            pygame.display.update()

    def show_start_screen(self) -> None:
        self.screen.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 24)
        text = font.render('Loading...', False, (255, 255, 255))
        self.screen.blit(text, (20,10))
        pygame.display.update()
        timer(5)
        self.screen.fill(BLACK)
        brand_name = pygame.image.load('src/brand_name/1.png')
        rect = brand_name.get_rect()
        rect.center = self.screen_center
        self.screen.blit(brand_name, rect)
        pygame.display.update()
        timer(5)

    def show_menu_screen(self) -> None:
        self.m_btn_x = 320
        self.m_btn_y1 = 230
        self.m_btn_y2 = 160
        self.m_btn_y3 = 90
        while self.menu:
            self.screen.fill(BLACK)
            self.menu_btn1 = ButtonMenu('src/buttons_menu/1.png', self.screen_size[0] - 150, self.screen_size[1] - 190)
            self.screen.blit(self.menu_btn1.image, self.menu_btn1.rect)
            self.menu_btn2 = ButtonMenu('src/buttons_menu/2.png', self.screen_size[0] - 150, self.screen_size[1] - 120)
            self.screen.blit(self.menu_btn2.image, self.menu_btn2.rect)
            self.menu_btn3 = ButtonMenu('src/buttons_menu/3.png', self.screen_size[0] - 150, self.screen_size[1] - 50)
            self.screen.blit(self.menu_btn3.image, self.menu_btn3.rect)
            pygame.display.update()
            self.check_events()

    def check_events(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.menu:
                    self.click_in_menu(event)

    def click_in_menu(self, event) -> None:
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.menu_btn1.rect.collidepoint(event.pos):
                    self.new_game()
                    self.menu = False
                if self.menu_btn2.rect.collidepoint(event.pos):
                        self.menu = False
                if self.menu_btn3.rect.collidepoint(event.pos):
                        sys.exit()

    def new_game(self) -> None:
        self.money = 0
        self.level = 0
        self.experience = 0


if __name__ == '__main__':
    app = PixelFarm()
    app.run()