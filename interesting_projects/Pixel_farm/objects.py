from app import pygame

class FarmObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))
       self.hp = 5
       self.image_address = image

    def click_on_it(self) -> bool:
        self.hp -= 1
        print(self)
        if self.hp == 0:
            return True
        return False

    def __str__(self) -> str:
        return 'test'

    def __repl__(self) -> str:
        return 'test'

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

    def set_plant(self, plant: str) -> None:
        self.plant = plant
        self.image = pygame.image.load(f"src/planted_fields/{plant}.png")
        self.plant_stage = 1

class House(FarmObject):
    def __init__(self, x, y) -> None:
        super().__init__('src/buildings/house.png', x, y)

    def click_on_it(self) -> None:
        pass

class Character(FarmObject):
    pass