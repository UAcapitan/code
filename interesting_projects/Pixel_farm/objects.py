from app import pygame


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

class Shovel(FarmItem):
    pass