import pygame
import sys
import json
import tkinter as tk
import time
import random
import jsonpickle
from json import JSONEncoder

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def timer(n):
    t = time.time()
    while time.time() - t < n:
        pass

class FarmObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))
       self.hp = 5

    def click_on_it(self) -> bool:
        self.hp -= 1
        if self.hp == 0:
            return True
        return False

class ButtonMenu(FarmObject):
    pass

class Stone(FarmObject):
    pass

class Bush(FarmObject):
    pass

class Field(FarmObject):
    pass

class House(FarmObject):
    def __init__(self, x, y) -> None:
        super().__init__('src/buildings/house.png', x, y)

    def click_on_it(self) -> None:
        pass

class Character(FarmObject):
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

        self.elements_on_map = []

        self.money = 0
        self.level = 0
        self.experience = 0

        self.time_point = 0

        self.task = 0
        self.part_of_conversation = 1
        self.task_num = 0

        self.inventory = []

        self.special_inventory = ['']

    def run(self) -> None:
        '''
            Main function of game
        '''

        # Start screen showing
        # self.show_start_screen()
        self.menu = True
        self.show_menu_screen()
        while True:

            # Fill screen
            self.screen.fill(GREEN)

            # Events
            self.check_events()

            for e in self.elements_on_map:
                self.screen.blit(e.image, e.rect)

            # Inventory on bottom of screen
            self.inventory_botton_screen()

            self.tasks()

            # Updating of screen
            pygame.display.update()

    def show_start_screen(self) -> None:
        self.screen.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 24)
        text = font.render('Loading...', False, WHITE)
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
                    self.save_game()
                    sys.exit()
                if self.menu:
                    self.click_in_menu(event)
                else:
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if event.button == 1:
                    #         if self.menu_btn1.rect.collidepoint(event.pos):
                    #             self.menu = True
                    self.click_object(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        del self.elements_on_map[0]

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

        self.time_point = time.time()

        for i in range(random.randint(0, 10)):
            self.elements_on_map.append(Stone('src/stones/1.png', random.randint(30, self.screen_size[0]-30), random.randint(30, self.screen_size[1]-30)))
        for i in range(random.randint(0, 10)):
            self.elements_on_map.append(Stone('src/stones/2.png', random.randint(30, self.screen_size[0]-30), random.randint(30, self.screen_size[1]-30)))
        for i in range(random.randint(0, 10)):
            self.elements_on_map.append(Stone('src/stones/3.png', random.randint(30, self.screen_size[0]-30), random.randint(30, self.screen_size[1]-30)))

        for i in range(random.randint(0, 10)):
            self.elements_on_map.append(Bush('src/bushes/1.png', random.randint(30, self.screen_size[0]-30), random.randint(30, self.screen_size[1]-30)))

        self.elements_on_map.append(Field('src/fields/1.png', 50, 50))

        self.elements_on_map.append(House(700, 150))

    def inventory_botton_screen(self) -> None:
        pygame.draw.rect(self.screen, WHITE, 
            pygame.Rect(20, self.screen_size[1] - 70, self.screen_size[0] - 40, self.screen_size[1])
        )

    def click_object(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                garbage = []
                for i in self.elements_on_map:
                    if i.rect.collidepoint(event.pos):
                        if i.click_on_it():
                            garbage.append(i)

                if len(garbage) > 0:
                    del self.elements_on_map[self.elements_on_map.index(garbage[0])]
                            
    def save_game(self) -> None:
        with open('player_data.json', 'w') as file:
            json.dump({
                "player": 1,
                "elements_on_map": [jsonpickle.encode(i) for i in self.elements_on_map],
                "inventory": []
            }, file)

    def tasks(self):
        # Conditions for tasks
        if self.level == 0 and self.experience == 0 and time.time() - self.time_point > 3:
            print('It works')
            self.experience += 10
            self.task = 1
            self.time_point = time.time()

        # Conversations
        if self.task == 1:
            pygame.draw.rect(self.screen, WHITE, 
                pygame.Rect(0, self.screen_size[1] - 70, self.screen_size[0], self.screen_size[1])
            )
            font = pygame.font.SysFont('Comic Sans MS', 24)
            text = font.render('Hi! How are you? Are you a new farmer there?', False, BLACK)
            self.screen.blit(self.screen, (150, self.screen_size[1] - 55))
            if self.part_of_conversation == 1:
                text = font.render('Test', False, BLACK)
                self.screen.blit(text, (150, self.screen_size[1] - 27))
                # self.timer_for_conversation(10)
                pass
            if self.part_of_conversation == 2:
                # Show conversation
                # Show character
                # self.timer_for_conversation(10)
                pass
            if self.part_of_conversation == 3:
                # Show conversation
                # self.timer_for_conversation(10)
                pass
            character = Character('src/characters/1.png', 55, self.screen_size[1] - 55)
            self.screen.blit(
                character.image,
                character.rect
            )
            self.screen.blit(text, (150, 150))

    # def timer_for_conversation(self, n):
    #     if time.time() - self.time_point >= n:
    #         self.part_of_conversation += 1
    

if __name__ == '__main__':
    app = PixelFarm()
    app.run()