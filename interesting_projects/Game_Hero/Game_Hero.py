# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys
import random

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
        self.map = [
            [1,0,0,0,0,0,0,0,0,0],
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
        self.x = 0
        self.y = 0

    def updateMap(self, player):
        self.map[player.last_y][player.last_x] = 0
        self.map[player.y][player.x] = 1

    def updateMapEnemy(self, enemy):
        self.map[enemy.y][enemy.x] = 2

class PlayerGame:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.last_x = 0
        self.last_y = 0

    def playerRight(self):
        if self.x <= 8:
            self.x += 1
            self.last_x = self.x - 1
            self.last_y = self.y

    def playerLeft(self):
        if self.x > 0:
            self.x -= 1
            self.last_x = self.x + 1
            self.last_y = self.y

    def playerUp(self):
        if self.y > 0:
            self.y -= 1
            self.last_y = self.y + 1
            self.last_x = self.x

    def playerDown(self):
        if self.y <= 8:
            self.y += 1
            self.last_y = self.y - 1
            self.last_x = self.x

class EnemyGame:
    def __init__(self, x, y):
        self.x = x
        self.y = y

map_game = MapGame()
player_game = PlayerGame()
enemy_game = []

enemy_game.append(EnemyGame(random.randint(0,8), random.randint(0,8)))
map_game.updateMapEnemy(enemy_game[0])

while True:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d:
                player_game.playerRight()
            elif i.key == pygame.K_a:
                player_game.playerLeft()
            elif i.key == pygame.K_w:
                player_game.playerUp()
            elif i.key == pygame.K_s:
                player_game.playerDown()
            map_game.updateMap(player_game)

    screen.fill(GREEN_COLOR)

    for i in map_game.map:
        for j in i:
            if j == 1:
                pygame.draw.rect(screen, LIME_COLOR, (map_game.x,map_game.y,20,20))
            if j == 2:
                pygame.draw.rect(screen, RED_COLOR, (map_game.x,map_game.y,20,20))
            if j == 3:
                pygame.draw.rect(screen, BLUE_COLOR, (map_game.x,map_game.y,20,20))
            map_game.x += 20
        map_game.x = 0
        map_game.y += 20
    
    map_game.y = 0

    pygame.display.update()