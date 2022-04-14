from app import pygame

class FarmObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect(center=(x,y))
       self.hp = 5

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
    pass

class House(FarmObject):
    def __init__(self, x, y) -> None:
        super().__init__('src/buildings/house.png', x, y)

    def click_on_it(self) -> None:
        pass
