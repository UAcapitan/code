from app import pygame
from app import time


class BaseFarmObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))
       self.image_address = image

    def info(self) -> dict:
        return {}

class FarmObject(BaseFarmObject):
    def __init__(self, image, x: int, y: int, hp: int) -> None:
        super().__init__(image, x, y)
        self.hp = hp
        self.full_hp = hp

    def click_on_it(self) -> bool:
        self.hp -= 1
        if self.hp == 0:
            return True
        return False

class FarmItem(BaseFarmObject):
    def __init__(self, name, x, y) -> None:
        self.name = name
        img_address = f"src/items/{self.name}.png"
        super().__init__(img_address, x, y)
    
    def __str__(self) -> str:
        return self.name

    def __repl__(self) -> str:
        return self.name

class ButtonMenu(BaseFarmObject):
    pass

class Stone(FarmObject):
    def info(self) -> dict:
        return {
            'name': 'Stone',
            'image': self.image,
            'hp': self.hp,
            'full_hp': self.full_hp,
            'text': [
                'This is just a stone.',
                '',
                ''
            ]
        }

class Bush(FarmObject):
    def info(self) -> dict:
        return {
            'name': 'Bush',
            'image': self.image,
            'hp': self.hp,
            'full_hp': self.full_hp,
            'text': [
                'Not big green bush.',
                'You can harvest sometimes.',
                ''
            ]
        }

class Tree(FarmObject):
    def info(self) -> dict:
        return {
            'name': 'Three',
            'image': self.image,
            'hp': self.hp,
            'full_hp': self.full_hp,
            'text': [
                'Big handsome tree.',
                '',
                ''
            ]
        }

class Field(FarmObject):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)
        self.plant = None
        self.plant_stage = 0
        self.time_point = time.time()
        self.time_for_growing = 0

    def set_plant(self, plant: str, time_grow: int) -> None:
        self.plant = plant
        self.image = pygame.image.load(f"src/planted_fields/{plant}_1.png")
        self.plant_stage = 1
        self.time_point = time.time()
        self.image_address = f"src/planted_fields/{plant}_1.png"
        self.time_for_growing = time_grow

    def grow(self) -> None:
        if self.plant_stage > 0 or self.plant_stage < 3:
            if time.time() - self.time_point > self.time_for_growing:
                if self.plant_stage == 1:
                    self.image = pygame.image.load(f"src/planted_fields/{self.plant}_2.png")
                    self.plant_stage += 1
                    self.image_address = f"src/planted_fields/{self.plant}_2.png"
                elif self.plant_stage == 2:
                    self.image = pygame.image.load(f"src/planted_fields/{self.plant}_3.png")
                    self.plant_stage += 1
                    self.image_address = f"src/planted_fields/{self.plant}_3.png"
                
                self.time_point = time.time()

    def get_harvest(self) -> str:
        self.image = pygame.image.load(f"src/fields/1.png")
        plant = self.plant
        self.plant = None
        self.plant_stage = 0
        self.time_point = time.time()
        self.time_for_growing = 0
        self.image_address = f"src/fields/1.png"
        return plant

    def info(self) -> dict:
        if self.plant == None:
            return {
                'name': 'Field',
                'image': self.image,
                'hp': self.hp,
                'full_hp': self.full_hp,
                'text': [
                    'Just empty field.',
                    '',
                    ''
                ]
            }
        else:
            stage = self.plant_stage
            if stage == 1:
                stage = 'Newly planted.'
            elif stage == 2:
                stage = 'Growing.'
            else:
                stage = 'You can harvest.'
            return {
                'name': f"Field - {self.plant}",
                'image': self.image,
                'hp': self.hp,
                'full_hp': self.full_hp,
                'text': [
                    'Just planted field.',
                    'Wait for harvest.',
                    f"Stage right now: {stage}"
                ]
            }

class House(FarmObject):
    def __init__(self, x, y) -> None:
        super().__init__('src/buildings/house.png', x, y, 0)

    def click_on_it(self) -> None:
        pass

    def info(self) -> dict:
        return {
            'name': 'House',
            'image': self.image,
            'hp': '-',
            'full_hp': '-',
            'text': [
                'Your house ',
                '',
                ''
            ]
        }

class Character(FarmObject):
    pass