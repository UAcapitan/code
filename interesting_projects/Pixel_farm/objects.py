from matplotlib import image
from app import pygame
from app import time


class BaseFarmObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))
       self.image_address = image

class FarmObject(BaseFarmObject):
    def __init__(self, image, x, y) -> None:
        super().__init__(image, x, y)
        self.hp = 5

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

class ButtonMenu(FarmObject):
    pass

class Stone(FarmObject):
    pass

class Bush(FarmObject):
    pass

class Field(FarmObject):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
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

class House(FarmObject):
    def __init__(self, x, y) -> None:
        super().__init__('src/buildings/house.png', x, y)

    def click_on_it(self) -> None:
        pass

class Character(FarmObject):
    pass