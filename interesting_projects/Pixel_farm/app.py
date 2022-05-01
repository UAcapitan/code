from django.conf import settings
import pygame
import sys
import json
import tkinter as tk
import time
import random
import jsonpickle
import collections
import os
from json import JSONEncoder
from typing import Union

# Special app modules
from objects import *
from tasks import generate_task
from conversations import generate_conversation

pygame.init()
pygame.font.init()

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (153, 153, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 153)
GRAY = (230, 230, 230)
ORANGE = (255, 165, 0)

# Just a timer for loading
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

        self.check_needed_files()

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

        self.money = 50
        self.level = 0
        self.experience = 0

        self.time_point = 0

        self.task = 0
        self.part_of_conversation = 0
        self.task_num = 0

        self.inventory = []

        self.inventory_count = []

        self.special_inventory = []

        self.energy = 100
        self.energy_time_point = time.time()

        self.farm_window = False

        self.item = False

        self.harvest = False

        self.tasks_list = []

        self.shop_items_dict = {
            'seeds_of_wheat': 1,
            'seeds_of_carrot': 2,
            'seeds_of_potato': 3,
            'seeds_of_grass': 3,
            'seeds_of_onion': 5,
        }

        self.shop_items_list = [i for i in self.shop_items_dict]

        self.center_of_map = [0, 0]

        self.timer_task = 0

        self.buttons_tasks = []

        self.main_screen = True

        self.button_in_farm_window = 1

        self.creative_recepies = {
            'chest': {
                "wood": 3,
                "stone": 2,
                "energy": 25
            }
        }

        self.buttons_in_shop = []

        self.information_window = False

        self.element_for_information = {}

    # Main game logic
    def run(self) -> None:
        '''
            Main function of game
        '''

        # Start screen showing
        # self.show_start_screen()
        self.menu = True
        while True:

            self.clock.tick(FPS)

            if self.menu:
                self.show_menu_screen()
                continue
            
            self.regenerate_energy()
            self.grow()
            self.draw_all()
            self.timer_for_adding_task()

    # Draw
    def draw_all(self) -> None:
        # Fill screen
        self.screen.fill(GREEN)

        # Events
        self.check_events()

        for e in self.elements_on_map:
            self.screen.blit(e.image, e.rect)

        self.draw_available_field()

        if self.farm_window:
            self.draw_window(20, 20, self.screen_size[0] - 40, self.screen_size[1] - 40)
        else:
            if self.information_window:
                self.draw_information_window()
            else:
                self.draw_inventory()
                self.draw_status_player()

        # Updating of screen
        pygame.display.update()

    def draw_interface(self) -> None:
        # Inventory on bottom of screen
        self.inventory_bottom_screen()

        self.tasks()

    def draw_energy_line(self) -> None:
        pygame.draw.rect(self.screen, YELLOW, 
            pygame.Rect(self.screen_size[0] - 210, 30, self.energy*2, 20)
        )
        pygame.draw.rect(self.screen, DARK_YELLOW, 
            pygame.Rect(self.screen_size[0] - 210 + self.energy*2, 30, 200-self.energy*2, 20)
        )

    def draw_experience_line(self) -> None:
        p = ((self.level + 1) * 100) / 100
        w = self.experience // p

        pygame.draw.rect(self.screen, BLUE, 
            pygame.Rect(self.screen_size[0] - 210, 60, w, 5)
        )
        pygame.draw.rect(self.screen, DARK_BLUE, 
            pygame.Rect(self.screen_size[0] - 210 + w, 60, 100-w, 5)
        )

    def draw_available_field(self):
        if self.item == 1:
            if self.check_collision() and self.check_energy(20):
                image = pygame.image.load('src/fields/00.png')
            else:
                image = pygame.image.load('src/fields/01.png')

            rect = image.get_rect()
            rect.center = pygame.mouse.get_pos()
            self.screen.blit(image, rect)

    def draw_window(self, x: int, y: int, w: int, h: int) -> None:
        if self.menu == False:
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(x, y, w, h))
            self.draw_exit_button(x + w - 10, y + 10)
            self.draw_farm_window_menu(h)
            if self.button_in_farm_window == 1:
                self.draw_task_window(x, y, w, h)
            elif self.button_in_farm_window == 2:
                self.draw_farm_shop(x, y, w, h)
            elif self.button_in_farm_window == 3:
                self.draw_farm_creative(x, y, w, h)

    def draw_task_window(self, x: int, y: int, w: int, h: int) -> None:
        self.buttons_tasks = []
        y1 = 70
        for i in self.pagination_of_tasks(1):
            rect = pygame.Rect(x + 70, y + y1 , w - 90, h/4)
            if len(self.buttons_tasks) < 4:
                self.buttons_tasks.append(rect)

            flag = True
            for j in i["items"]:
                if not j in self.inventory:
                    flag = False

            if flag:      
                pygame.draw.rect(self.screen, GREEN, rect)
            else:
                pygame.draw.rect(self.screen, GRAY, rect)

            image = pygame.image.load(f"src/characters/{i['name']}.png")
            rect = pygame.Rect(x + 70, y + y1, 128, 128)
            self.screen.blit(image, rect)
            font = pygame.font.SysFont('Comic Sanc MS', 24)
            self.screen.blit(font.render(f"{i['name']}", False, BLACK), (x + 250, y + y1 + 10))
            self.screen.blit(font.render(f"{i['text']}", False, BLACK), (x + 250, y + y1 + 50))

            image = pygame.image.load('src/money/1.png')
            rect = image.get_rect()
            rect.center = (x + 884, y + y1 + 60)
            self.screen.blit(image, rect)

            self.screen.blit(font.render(f"{i['price']}", False, YELLOW), (x + 900, y + y1 + 53))

            x1 = 0
            for j in i['items']:
                image = pygame.image.load(f'src/items/{j}.png')
                rect = image.get_rect()
                rect.center = (x + 250 + x1, y + y1 + 120)
                self.screen.blit(image, rect)
                x1 += 64

            y1 += h/4 + 10

    def draw_inventory(self) -> None:
        self.draw_interface()
        self.draw_choiced_block_of_item()
        self.draw_items_in_bottom_inventory()
        self.draw_inventory_count()

    def draw_items_in_bottom_inventory(self) -> None:
        x = 20
        w = (self.screen_size[0] - 40) / 10
        for i in self.inventory:
            image = pygame.image.load(f"src/items/{i}.png")
            rect = image.get_rect()
            rect.center = (x + w / 2, self.screen_size[1] - 30)
            self.screen.blit(image, rect)
            x += w

    def draw_choiced_block_of_item(self) -> None:
        if self.item != False:
            w = (self.screen_size[0] - 40) / 10
            x = 20 + w * (self.item - 1)
            
            pygame.draw.rect(self.screen, GREEN, 
                pygame.Rect(x, self.screen_size[1] - 70, w, self.screen_size[1])
            )

            pygame.draw.rect(self.screen, WHITE, 
                pygame.Rect(x+3, self.screen_size[1] - 67, w-5, self.screen_size[1])
            )

    def draw_inventory_count(self) -> None:
        font = pygame.font.SysFont('Comic Sans MS', 24)
        x = 110
        w = (self.screen_size[0] - 40) / 10
        for i in self.inventory:
            if self.inventory_count[self.inventory.index(i)] == -1:
                text = font.render('', False, BLACK)
            else:
                text = font.render(str(self.inventory_count[self.inventory.index(i)]), False, BLACK)
            self.screen.blit(text, (x, self.screen_size[1] - 30))
            x += w

    def draw_level(self) -> None:
        pygame.draw.circle(self.screen, WHITE, (self.screen_size[0] - 250, 50), 25, 3)
        font = pygame.font.SysFont('Comic Sans MS', 22)
        text = font.render(str(self.level), False, WHITE)
        self.screen.blit(text, (self.screen_size[0] - 257, 35))

    def draw_status_player(self) -> None:
        self.draw_energy_line()
        self.draw_experience_line()
        self.draw_level()
        self.draw_money()

    def draw_money(self) -> None:
        font = pygame.font.SysFont('Comic Sans MS', 18)
        text = font.render(str(self.money), False, YELLOW)
        self.screen.blit(text, (self.screen_size[0] - 195, 72))
        image = pygame.image.load('src/money/1.png')
        rect = image.get_rect()
        rect.center = (self.screen_size[0] - 205, 85)
        self.screen.blit(image, rect)

    def draw_farm_window_menu(self, h: int) -> None:
        pygame.draw.rect(self.screen, BLUE, pygame.Rect(20, 20, 64, h))
        menu = [
            'tasks',
            'shop',
            'creative'
        ]
        n = 64 * (self.button_in_farm_window - 1)
        pygame.draw.rect(self.screen, ORANGE, pygame.Rect(20, 20 + n, 64, 64))
        y1 = 0
        for i in menu:
            image = pygame.image.load(f"src/farm_menu/{i}.png")
            rect = image.get_rect()
            rect.center = (52, 52 + y1)
            self.screen.blit(image, rect)
            y1 += 64
        
    def draw_farm_shop(self, x: int, y: int, w: int, h: int) -> None:
        x1 = 0
        y1 = 0
        n = 0
        flag = False
        if len(self.buttons_in_shop) < len(self.shop_items_dict):
            flag = True
            self.buttons_in_shop = []
        for i in self.shop_items_dict:
            image = pygame.image.load(f"src/items/{i}.png")
            rect = pygame.Rect(x + 80 + x1, y + 20 + y1, 64, 64)
            if self.money >= self.shop_items_dict[i]:
                pygame.draw.rect(self.screen, GREEN, rect)
            else:
                pygame.draw.rect(self.screen, GRAY, rect)
            if flag:
                self.buttons_in_shop.append(rect)
            self.screen.blit(image, rect)
            font = pygame.font.SysFont('Comic Sanc MS', 24)
            self.screen.blit(font.render(f"{self.shop_items_dict[i]}", False, YELLOW), (x + 125 + x1, y + y1 + 70))
            x1 += 64
            n += 1
            if n == 9:
                x1 = 0
                n = 0
                y += 64

    def draw_farm_creative(self, x: int, y: int, w: int, h: int) -> None:
        for i in self.creative_recipes:
            image = pygame.image.load(f"src/characters/{i}.png")
            rect = pygame.Rect(x + 70, y + y1, 128, 128)
            self.screen.blit(image, rect)
            font = pygame.font.SysFont('Comic Sanc MS', 24)
            self.screen.blit(font.render(f"{i['name']}", False, BLACK), (x + 250, y + y1 + 10))
            y1 += 10

    def draw_information_window(self) -> None:
        pygame.draw.rect(self.screen, WHITE, 
            pygame.Rect(20, 20, self.screen_size[0] - 40, self.screen_size[1] - 40)
        )
        item = self.element_for_information
        self.draw_exit_button(self.screen_size[0] - 28, 28)
        font = pygame.font.SysFont('Comic Sanc MS', 24)
        text = font.render(item['name'], False, BLACK)
        self.screen.blit(text, (90, 50))

    def draw_exit_button(self, x: int, y: int) -> None:
        image = pygame.image.load("src/buttons/exit.png")
        rect = image.get_rect()
        rect.center = (x, y)
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
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.save_game()
                            self.menu = True

                if self.main_screen:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.increase_money(10)
                        if event.key == pygame.K_1:
                            self.set_item(1)
                        elif event.key == pygame.K_2:
                            self.set_item(2)
                        elif event.key == pygame.K_3:
                            self.set_item(3)
                        elif event.key == pygame.K_4:
                            self.set_item(4)
                        elif event.key == pygame.K_5:
                            self.set_item(5)
                        elif event.key == pygame.K_6:
                            self.set_item(6)
                        elif event.key == pygame.K_7:
                            self.set_item(7)
                        elif event.key == pygame.K_8:
                            self.set_item(8)
                        elif event.key == pygame.K_9:
                            self.set_item(9)
                        elif event.key == pygame.K_0:
                            self.set_item(10)
                else:
                    if self.farm_window:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                self.change_button_in_farm_window(1)
                            elif event.key == pygame.K_2:
                                self.change_button_in_farm_window(2)
                            elif event.key == pygame.K_3:
                                self.change_button_in_farm_window(3)

                self.check_moving_map()
                self.click_with_mouse(event)

                # self.click_when_conversation(event)
    
    def check_energy(self, n:int) -> bool:
        if self.energy - n >= 0:
            return True
        return False

    def check_collision(self) -> bool:
        mouse = pygame.mouse.get_pos()
        rect = pygame.Rect(mouse[0]-32, mouse[1]-32, 64, 64)
        for i in self.elements_on_map:
            if i.rect.colliderect(rect):
                return False
        return True
    
    def check_collision_for_numbers(self, x: int, y: int) -> bool:
        rect = pygame.Rect(x, y, 64, 64)
        for i in self.elements_on_map:
            if i.rect.colliderect(rect):
                return False
        return True

    def check_count_inventory(self) -> None:
        if self.inventory_count[self.item - 1] == 0:
            del self.inventory[self.item - 1]
            del self.inventory_count[self.item - 1]

    def check_moving_map(self) -> None:
        if not self.farm_window:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.move_map([0, 10])
            if keys[pygame.K_a]:
                self.move_map([10, 0])
            if keys[pygame.K_s]:
                self.move_map([0, -10])
            if keys[pygame.K_d]:
                self.move_map([-10, 0])

    # All clicks
    def click_in_menu(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.menu_btn1.rect.collidepoint(event.pos):
                    self.new_game()
                    self.menu = False
                if self.menu_btn2.rect.collidepoint(event.pos):
                        self.load_game()
                        self.menu = False
                if self.menu_btn3.rect.collidepoint(event.pos):
                        sys.exit()

    def click_when_conversation(self, event) -> None:
        if self.task > 0:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.next_part_of_conversation()

    def click_for_make_field(self) -> None:
        if self.check_collision():
            if self.decrease_energy(20):
                self.increase_experience(25)
                x, y = pygame.mouse.get_pos()
                self.elements_on_map.append(Field('src/fields/1.png', x, y))

    def click_to_plant(self, seeds, time_grow) -> None:
        mouse = pygame.mouse.get_pos()
        for i in self.elements_on_map:
            if isinstance(i, Field):
                if i.rect.collidepoint(mouse):
                    if i.plant_stage == 0:
                        if self.decrease_energy(10):
                            i.set_plant(seeds, time_grow)
                            self.increase_experience(10)
                            self.decrease_count_of_item_inventory()

    def click_conditions(self, event) -> None:
        try:
            item = self.inventory[self.item - 1]
        except:
            item = ''

        if item == 'shovel':
            self.click_for_make_field()

        if item == 'loupe':
            self.use_loupe(event)

        elif item == 'pickaxe':
            self.use_pickaxe(event)

        elif item == 'seeds_of_wheat':
            self.click_to_plant('wheat', 60)

        elif item == 'seeds_of_carrot':
            self.click_to_plant('carrot', 80)

        elif item == 'seeds_of_potato':
            self.click_to_plant('potato', 100)

        elif item == 'seeds_of_grass':
            self.click_to_plant('grass', 30)

        elif item == 'seeds_of_onion':
            self.click_to_plant('onion', 120)

        elif item == 'seeds_of_cucumber':
            self.click_to_plant('cucumber', 130)

    def click_at_field(self, event) -> None:
        for i in self.elements_on_map:
                if isinstance(i, Field):
                    if i.rect.collidepoint(event.pos):
                        if self.check_inventory(i.plant):
                            if i.plant_stage == 3:
                                harvest = i.get_harvest()
                                self.add_to_inventory(harvest)
                                self.increase_experience(25)

    def click_with_mouse(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click_conditions(event)
                self.click_at_field(event)
                
                if not self.farm_window:
                    for i in self.elements_on_map:
                        if isinstance(i, House):
                            if i.rect.collidepoint(event.pos):
                                self.farm_window = True
                                self.main_screen = False
                else:
                    if pygame.Rect(20 + self.screen_size[0] - 90, 20, 50, 50).collidepoint(event.pos):
                        self.farm_window = False
                        self.main_screen = True

        self.click_on_tasks(event)
        self.click_on_item_in_shop(event)

    def click_on_tasks(self, event) -> None:
        if self.farm_window and self.button_in_farm_window == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Done task
                if event.button == 1:
                    if self.farm_window:
                        for i in self.buttons_tasks:
                            if i.collidepoint(event.pos):
                                item = self.tasks_list[self.buttons_tasks.index(i)]
                                if self.check_needed_item_in_inventory(item["items"]):
                                    self.increase_experience(50)
                                    self.money += item["price"]
                                    del self.tasks_list[self.buttons_tasks.index(i)]

                # Delete task
                if event.button == 3:
                    if self.farm_window:
                        for i in self.buttons_tasks:
                            if i.collidepoint(event.pos):
                                del self.tasks_list[self.buttons_tasks.index(i)]

    def click_on_item_in_shop(self, event) -> None:
        if self.farm_window and self.button_in_farm_window == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in self.buttons_in_shop:
                        if i.collidepoint(event.pos):
                            ind = self.buttons_in_shop.index(i)
                            item = self.shop_items_list[ind]
                            price = self.shop_items_dict[item]
                            if self.decrease_money(price):
                                if self.check_inventory(item):
                                    self.add_to_inventory(item)                          

    # Start game
    def new_game(self) -> None:
        self.money = 50
        self.level = 0
        self.experience = 0
        self.elements_on_map = []

        self.time_point = time.time()

        self.elements_on_map.append(House(700, 150))

        self.inventory = [
            'shovel',
            'loupe',
            'pickaxe',
            # 'seeds_of_wheat',
            # 'seeds_of_carrot',
            # 'seeds_of_potato',
            # 'seeds_of_grass',
            # 'seeds_of_onion',
            # 'seeds_of_cucumber',
            'wheat',
            'carrot',
            'potato',
            'grass',
            'onion',
            'cucumber',
        ]

        self.inventory_count = [
            -1,
            -1,
            -1,
            10,
            10,
            3,
            3,
            3,
            3
        ]

        for i in range(random.randint(0, 100)):
            coordinates = self.generate_two_coordinates()
            if coordinates:
                self.elements_on_map.append(Stone('src/stones/1.png', coordinates[0], coordinates[1]))
        for i in range(random.randint(0, 100)):
            coordinates = self.generate_two_coordinates()
            if coordinates:
                self.elements_on_map.append(Stone('src/stones/2.png', coordinates[0], coordinates[1]))
        for i in range(random.randint(0, 100)):
            coordinates = self.generate_two_coordinates()
            if coordinates:
                self.elements_on_map.append(Stone('src/stones/3.png', coordinates[0], coordinates[1]))

        for i in range(random.randint(0, 100)):
            coordinates = self.generate_two_coordinates()
            if coordinates:
                self.elements_on_map.append(Bush('src/bushes/1.png', coordinates[0], coordinates[1]))

        # TODO do it later

        # for i in range(random.randint(0, 10)):
        #     coordinates = self.generate_two_coordinates()
        #     self.elements_on_map.append(Tree('src/trees/1.png', coordinates[0], coordinates[1]))

        self.timer_task = time.time()

        self.buttons_tasks = []

    # Inventory
    def inventory_bottom_screen(self) -> None:
        pygame.draw.rect(self.screen, WHITE, 
            pygame.Rect(20, self.screen_size[1] - 70, self.screen_size[0] - 40, self.screen_size[1])
        )

    def set_item(self, n:int) -> None:
        if self.item != n:
            self.item = n
        elif self.item == n:
            self.item = False

    def add_to_inventory(self, item: str) -> None:
        if item:
            if item in self.inventory:
                self.inventory_count[self.inventory.index(item)] += 1
            else:
                self.inventory.append(item)
                self.inventory_count.append(1)

    def check_inventory(self, item: str) -> bool:
        if len(self.inventory) <= 9 or item in self.inventory:
            return True
        return False

    def check_needed_item_in_inventory(self, products: list) -> bool:
        flag = True

        dict_products = dict(collections.Counter(products))
        
        for i, j in dict_products.items():
            if not i in self.inventory:
                flag = False
            else:
                if self.inventory_count[self.inventory.index(i)] < j:
                    flag = False

        if flag:
            for i in products:
                self.inventory_count[self.inventory.index(i)] -= 1

            inv = []
            inv_count = []
            ind = 0

            for i in self.inventory:
                if self.inventory_count[ind] == 0:
                    inv.append(i)
                    inv_count.append(ind)
                ind += 1

            
            for i in reversed(inv_count):
                del self.inventory_count[i]

            for i in inv:
                n = self.inventory.index(i)
                del self.inventory[n]
            
            return True
        return False

    # Saving           
    def save_game(self) -> None:
        with open('player_data.json', 'w') as file:
            json.dump({
                "player": 1,
                "elements_on_map": [jsonpickle.encode(i) for i in self.elements_on_map],
                "money": self.money,
                "level": self.level,
                "experience": self.experience,
                "time_point": self.time_point,
                "task": self.task,
                "part_of_conversation": self.part_of_conversation,
                "task_num": self.task_num,
                "inventory": self.inventory,
                'inventory_count': self.inventory_count,
                "energy": self.energy,
                "center_of_map": self.center_of_map,
                "tasks_list": self.tasks_list,
                "timer_task": self.timer_task,
                "item": self.item,
            }, file)

    def load_game(self) -> None:
        with open('player_data.json', 'r') as file:
            player_data = json.load(file)

        self.elements_on_map = [jsonpickle.decode(i) for i in player_data["elements_on_map"]]

        for i in range(len(self.elements_on_map)):
            self.elements_on_map[i].image = pygame.image.load(self.elements_on_map[i].image_address)

        self.money = player_data["money"]
        self.level = player_data["level"]
        self.experience = player_data["experience"]
        self.time_point = player_data["time_point"]
        self.task = player_data["task"]
        self.part_of_conversation = player_data["part_of_conversation"]
        self.task_num = player_data["task_num"]
        self.inventory = player_data["inventory"]
        self.energy = player_data["energy"]
        self.inventory_count = player_data["inventory_count"]
        self.center_of_map = player_data["center_of_map"]
        self.tasks_list = player_data["tasks_list"]
        self.timer_task = player_data["timer_task"]
        self.item = player_data["item"]

    # Conversations
    def tasks(self) -> None:
        # Conditions for tasks
        if self.level == 0 and self.experience == 0 and time.time() - self.time_point > 30:
            self.experience += 10
            self.task = 1
            self.time_point = time.time()

            # self.show_conversation()

    def next_part_of_conversation(self) -> None:
        self.part_of_conversation += 1

    def show_conversation(self) -> None:
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

    # Decreasing
    def decrease_energy(self, n:int) -> bool:
        if self.check_energy(n):
            self.energy -= n
            return True
        return False

    def decrease_count_of_item_inventory(self) -> None:
        if self.inventory_count[self.item - 1] > 0:
            self.inventory_count[self.item - 1] -= 1
            self.check_count_inventory()

    def decrease_money(self, n: int) -> bool:
        if self.money - n >= 0:
            self.money -= n
            return True
        return False

    # Increase
    def regenerate_energy(self) -> None:
        if time.time() - self.energy_time_point > 1:
            if self.energy < 100:
                self.energy += 1
                self.energy_time_point = time.time()

    def increase_experience(self, n:int) -> None:
        self.experience += n
        if self.experience > ((self.level + 1) * 100):
            self.experience -= ((self.level + 1) * 100)
            self.increase_level()

    def increase_level(self) -> None:
        self.level += 1

    def increase_money(self, n: int) -> None:
        self.increase_experience(10)
        self.money += n
    
    # Generate
    def generate_two_coordinates(self) -> Union[tuple, bool]:
        x, y = random.randint(-300, self.screen_size[0]+300), random.randint(-300, self.screen_size[1]+300)
        if self.check_collision_for_numbers(x, y):
            return (x, y)
        return False

    # Look at something
    def loupe_use(self) -> None:
        self.draw_window(20, 20, 20, 20)

    # Growing of plant
    def grow(self) -> None:
        for i in self.elements_on_map:
            if isinstance(i, Field):
                if i.plant_stage > 0:
                    i.grow()

    # Moving
    def move_map(self, n: list) -> None:
        flag = True
        if n[0] < 0 and self.center_of_map[0] <= -300:
            flag = False
        if n[0] > 0 and self.center_of_map[0] >= 300:
            flag = False
        if n[1] < 0 and self.center_of_map[1] <= -300:
            flag = False
        if n[1] > 0 and self.center_of_map[1] >= 300:
            flag = False

        if flag:
            self.center_of_map[0] += n[0]
            self.center_of_map[1] += n[1]
            for i in self.elements_on_map:
                rect = i.rect
                rect[0] += n[0]
                rect[1] += n[1]
                i.rect = rect

    # Tasks
    def add_task(self) -> None:
        if len(self.tasks_list) < 4:
            self.tasks_list.append(generate_task(self.level))

    def pagination_of_tasks(self, n: int) -> list:
        n1 = n * 3
        return self.tasks_list[n1 - 3:n1]

    def timer_for_adding_task(self) -> None:
        if time.time() - self.timer_task > 3:
            self.add_task()
            self.timer_task = time.time()

    def change_button_in_farm_window(self, n: int) -> None:
        self.button_in_farm_window = n

    # Work with files
    def check_needed_files(self) -> bool:
        if not os.path.exists("settings.json"):
            with open("settings.json", "w") as file:
                settings_default = {
                    "fullscreen": 1,
                }
                json.dump(settings_default, file)

        if not os.path.exists("player_data.json"):
            with open("player_data.json", "w") as file:
                data = {}
                json.dump(data, file)

    # Loupe
    def use_loupe(self, event):
        for i in self.elements_on_map:
            if i.rect.collidepoint(event.pos):
                self.information_window = True
                self.element_for_information = i.info()

    # Pickaxe
    def use_pickaxe(self, event):
        garbage = []
        for i in self.elements_on_map:
            if i.rect.collidepoint(event.pos):
                if self.check_energy(5):
                    if isinstance(i, Stone):
                        if self.check_inventory('stone'):
                            if i.click_on_it():
                                self.add_to_inventory('stone')
                                self.energy -= 5
                                self.increase_experience(10)
                                garbage.append(i)
        
        if len(garbage) > 0:
                del self.elements_on_map[self.elements_on_map.index(garbage[0])]

if __name__ == '__main__':
    app = PixelFarm()
    app.run()