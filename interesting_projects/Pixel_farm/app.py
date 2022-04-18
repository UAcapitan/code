import pygame
import sys
import json
import tkinter as tk
import time
import random
import jsonpickle
from json import JSONEncoder
from typing import Union

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
YELLOW = (255, 255, 0)
DARK_YELLOW = (153, 153, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 153)

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

        self.inventory = [
            'shovel',
            'loupe',
            'pickaxe',
            'seeds_of_wheat',
            'seeds_of_carrot',
            'seeds_of_potato',
        ]

        self.inventory_count = [
            -1,
            -1,
            -1,
            10,
            10,
            3
        ]

        self.special_inventory = []

        self.energy = 100
        self.energy_time_point = time.time()

        self.farm_window = False

        self.item = False

        self.harvest = False

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
        self.draw_energy_line()
        self.draw_experience_line()
        self.draw_choiced_block_of_item()
        self.draw_items_in_bottom_inventory()
        self.draw_inventory_count()
        self.draw_level()

        if self.farm_window:
            self.draw_window(20, 20, self.screen_size[0] - 40, self.screen_size[1] - 40)

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

    def draw_elements_on_farm_window(self) -> None:
        pass

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        del self.elements_on_map[0]
                    elif event.key == pygame.K_1:
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

                    self.check_moving_map(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click_conditions(event)
                        self.click_at_field(event)
                        
                        # for i in self.elements_on_map:
                        #     if isinstance(i, House):
                        #         x, y = pygame.mouse.get_pos()
                        #         if i.rect.collidepoint(x, y):
                        #             self.farm_window = True

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

    def check_moving_map(self, event) -> None:
        if event.key == pygame.K_w:
            self.move_map([0, 10])
        elif event.key == pygame.K_a:
            self.move_map([10, 0])
        if event.key == pygame.K_s:
            self.move_map([0, -10])
        if event.key == pygame.K_d:
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
        if self.item == 1:
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
        self.harvest = False
        if item == 'shovel':
            self.click_for_make_field()

        if item == 'loupe':
            self.harvest = True

        elif item == 'pickaxe':
            garbage = []
            for i in self.elements_on_map:
                if i.rect.collidepoint(event.pos):
                    if self.check_energy(5):
                        if i.click_on_it():
                            self.energy -= 5
                            self.increase_experience(10)
                            garbage.append(i)
            
            if len(garbage) > 0:
                    del self.elements_on_map[self.elements_on_map.index(garbage[0])]

        elif item == 'seeds_of_wheat':
            self.click_to_plant('wheat', 60)

        elif item == 'seeds_of_carrot':
            self.click_to_plant('carrot', 80)

        elif item == 'seeds_of_potato':
            self.click_to_plant('potato', 100)

    def click_at_field(self, event) -> None:
                    for i in self.elements_on_map:
                        if isinstance(i, Field):
                            if i.rect.collidepoint(event.pos):
                                if i.plant_stage == 3:
                                    harvest = i.get_harvest()
                                    if harvest:
                                        if harvest in self.inventory:
                                            self.inventory_count[self.inventory.index(harvest)] += 1
                                        else:
                                            self.inventory.append(harvest)
                                            self.inventory_count.append(1)
                                    self.increase_experience(25)

    # Start game
    def new_game(self) -> None:
        self.money = 0
        self.level = 0
        self.experience = 0
        self.elements_on_map = []

        self.time_point = time.time()

        self.elements_on_map.append(House(700, 150))


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
                "energy": self.energy
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

    # Conversations
    def tasks(self) -> None:
        # Conditions for tasks
        if self.level == 0 and self.experience == 0 and time.time() - self.time_point > 30:
            self.experience += 10
            self.task = 1
            self.time_point = time.time()

            self.show_conversation()

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
            print(self.energy)
            return True
        return False

    def decrease_count_of_item_inventory(self) -> None:
        if self.inventory_count[self.item - 1] > 0:
            self.inventory_count[self.item - 1] -= 1
            self.check_count_inventory()

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
    
    # Generate
    def generate_two_coordinates(self) -> Union[tuple, bool]:
        x, y = random.randint(-300, self.screen_size[0]+300), random.randint(-300, self.screen_size[1]+300)
        if self.check_collision_for_numbers(x, y):
            return (x, y)
        return False

    # Look at something
    def loupe_use(self) -> None:
        pass

    # Growing of plant
    def grow(self) -> None:
        for i in self.elements_on_map:
            if isinstance(i, Field):
                if i.plant_stage > 0:
                    i.grow()

    # Moving
    def move_map(self, n: list) -> None:
        for i in self.elements_on_map:
            rect = i.rect
            rect[0] += n[0]
            rect[1] += n[1]
            i.rect = rect

if __name__ == '__main__':
    app = PixelFarm()
    app.run()