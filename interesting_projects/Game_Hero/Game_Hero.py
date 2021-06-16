# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys

FPS = 10
GREEN_COLOR = [0, 128, 0]
LIME_COLOR = [0,255,0]
RED_COLOR = [255,0,0]
BLUE_COLOR = [0,0,255]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((200,200))

screen.fill(GREEN_COLOR)

pygame.display.update()

# 1 - player
# 2 - enemy
# 3 - bonus

class MapGame:

    def __init__(self):
        self.__map = [
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,3,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]
        self.__x = 0
        self.__y = 0

    def getMap(self):
        return self.__map
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

map_game = MapGame()

while True:

    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill(GREEN_COLOR)

    for i in map_game.getMap():
        for j in i:
            if j == 1:
                pygame.draw.rect(screen, LIME_COLOR, (map_game.getX(),map_game.getY(),20,20))
            if j == 2:
                pygame.draw.rect(screen, RED_COLOR, (map_game.getX(),map_game.getY(),20,20))
            if j == 3:
                pygame.draw.rect(screen, BLUE_COLOR, (map_game.getX(),map_game.getY(),20,20))
            map_game.setX(map_game.getX()+20)
        map_game.setX(0)
        map_game.setY(map_game.getY()+20)
    
    map_game.setY(0)

    pygame.display.update()