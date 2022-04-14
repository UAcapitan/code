import pygame
import sys
import json
import tkinter as tk
import time
import random
import jsonpickle
from json import JSONEncoder

# Special app modules
from objects import *
from tasks import *
from conversations import generate_conversation

pygame.init()
pygame.font.init()

FPS = 30

WHITE = (255, 255, 255)
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

        root = tk.Tk()

        self.clock = pygame.time.Clock()

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
        self.part_of_conversation = 0
        self.task_num = 0

        self.inventory = []

        self.special_inventory = ['']

        self.energy = 100

        self.tool = False

    # Main game logic
    def run(self) -> None:
        '''
            Main function of game
        '''

        # Start screen showing
        # self.show_start_screen()
        self.menu = True
        self.show_menu_screen()
        while True:

            self.clock.tick(FPS)

            self.draw_all()

    # Draw
    def draw_all(self) -> None:
        # Fill screen
        self.screen.fill(GREEN)

        # Events
        self.check_events()

        for e in self.elements_on_map:
            self.screen.blit(e.image, e.rect)

        self.draw_available_field()

        self.draw_interface()

        # Updating of screen
        pygame.display.update()

    def draw_interface(self) -> None:
        # Inventory on bottom of screen
        self.inventory_bottom_screen()

        self.tasks()

    def draw_energy(self) -> None:
        pygame.draw.rect()

    def draw_available_field(self):
        if self.tool == 1:
            if self.check_collision():
                image = pygame.image.load('src/fields/00.png')
            else:
                image = pygame.image.load('src/fields/01.png')

            rect = image.get_rect()
            rect.center = pygame.mouse.get_pos()
            self.screen.blit(image, rect)

    # Loading screen
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

    # Menu
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

    # Check
    def check_events(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game()
                    sys.exit()

                if self.menu:
                    self.click_in_menu(event)
                else:
                    self.click_object(event)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.menu = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        del self.elements_on_map[0]
                    elif event.key == pygame.K_1:
                        self.set_tool(1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click_for_make_field()

                self.click_when_conversation(event)

    def check_energy(self, n: int) -> bool:
        if self.energy > 0:
            if self.energy > n:
                return True
        return False
    
    def check_collision(self) -> None:
        mouse = pygame.mouse.get_pos()
        rect = pygame.Rect(mouse[0]-32, mouse[1]-32, 64, 64)
        for i in self.elements_on_map:
            if i.rect.colliderect(rect):
                return False
        return True
    
    # All clicks
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

    def click_when_conversation(self, event) -> None:
        if self.task > 0:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.next_part_of_conversation()

    def click_for_make_field(self) -> None:
        if self.tool == 1:
            if self.check_collision():
                x, y = pygame.mouse.get_pos()
                self.elements_on_map.append(Field('src/fields/1.png', x, y))

    def click_object(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                garbage = []
                for i in self.elements_on_map:
                    if i.rect.collidepoint(event.pos):
                        if self.check_energy(5):
                            if i.click_on_it():
                                self.energy -= 5
                                garbage.append(i)

                if len(garbage) > 0:
                    del self.elements_on_map[self.elements_on_map.index(garbage[0])]

    # Start game
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

    # Inventory
    def inventory_bottom_screen(self) -> None:
        pygame.draw.rect(self.screen, WHITE, 
            pygame.Rect(20, self.screen_size[1] - 70, self.screen_size[0] - 40, self.screen_size[1])
        )

    def set_tool(self, n:int) -> None:
        if self.tool != n:
            self.tool = n
        elif self.tool == n:
            self.tool = False

    # Saving           
    def save_game(self) -> None:
        with open('player_data.json', 'w') as file:
            json.dump({
                "player": 1,
                "elements_on_map": [jsonpickle.encode(i) for i in self.elements_on_map],
                "inventory": []
            }, file)

    # Conversations
    def tasks(self):
        # Conditions for tasks
        if self.level == 0 and self.experience == 0 and time.time() - self.time_point > 30:
            print('It works')
            self.experience += 10
            self.task = 1
            self.time_point = time.time()

            self.show_conversation()

    def next_part_of_conversation(self) -> None:
        self.part_of_conversation += 1

    def show_conversation(self):
        pygame.draw.rect(self.screen, WHITE, 
            pygame.Rect(0, self.screen_size[1] - 70, self.screen_size[0], self.screen_size[1])
        )
        font = pygame.font.SysFont('Comic Sans MS', 24)
        
        conversation_list_Max = generate_conversation('Max', 1)

        # Check lenght of list
        if self.part_of_conversation + 1 == len(conversation_list_Max):
            self.task = 0
            self.part_of_conversation == 0
        
        # Show phrase of character
        text = font.render(conversation_list_Max[self.part_of_conversation], False, BLACK)
        character = Character('src/characters/1.png', 55, self.screen_size[1] - 55)
        self.screen.blit(
            character.image,
            character.rect
        )
        self.screen.blit(text, (155, self.screen_size[1] - 45))

if __name__ == '__main__':
    app = PixelFarm()
    app.run()