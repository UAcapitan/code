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
DARK_BLUE_COLOR = [0,0,128]
BLUE_COLOR = [0,0,255]
WHITE_COLOR = [230,230,230]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400,250))

screen.fill(GREEN_COLOR)

pygame.display.update()

# 1 - player
# 2 - enemy
# 3 - bonus

class MapGame:
    def __init__(self):
        self.map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.x = 0
        self.y = 0

    def updateMapPlayer(self, player):
        self.map[player.last_y][player.last_x] = 0
        self.map[player.y][player.x] = 1

    def updateMapEnemy(self, enemy):
        self.map[enemy.last_y][enemy.last_x] = 0
        self.map[enemy.y][enemy.x] = 2

    def updateMapBonus(self, bonus):
        self.map[bonus.y][bonus.x] = 3

class PlayerGame:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.last_x = 0
        self.last_y = 0
        self.health = 100
        self.energy = 100

    def playerRight(self):
        if self.x <= 18:
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

    def damagePlayer(self, hp):
        self.health -= hp
        if self.health < 0:
            self.health = 0

    def useEnergyPlayer(self, en):
        self.energy -= en
        if self.energy < 0:
            self.energy = 0

class EnemyGame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y

    def enemyRight(self):
        if self.x <= 18:
            self.x += 1
            self.last_x = self.x - 1
            self.last_y = self.y

    def enemyLeft(self):
        if self.x > 0:
            self.x -= 1
            self.last_x = self.x + 1
            self.last_y = self.y

    def enemyUp(self):
        if self.y > 0:
            self.y -= 1
            self.last_y = self.y + 1
            self.last_x = self.x

    def enemyDown(self):
        if self.y <= 8:
            self.y += 1
            self.last_y = self.y - 1
            self.last_x = self.x

class BonusGame:
    def __init__(self, x, y):
        self.x = x
        self.y = y

map_game = MapGame()
player_game = PlayerGame()
enemy_game = []
bonus_game = []

enemy_game.append(EnemyGame(random.randint(0,18), random.randint(0,8)))
map_game.updateMapEnemy(enemy_game[0])

bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))
bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))
bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))

for b in bonus_game:
    map_game.updateMapBonus(b)

enemy_counter_time = 0

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
            elif i.key == pygame.K_e:
                player_game.damagePlayer(10)
            elif i.key == pygame.K_q:
                player_game.useEnergyPlayer(10)
            map_game.updateMapPlayer(player_game)

    if enemy_counter_time == 5:
        random_enemy_move = random.randint(0,4)
        if random_enemy_move == 0:
            enemy_game[0].enemyRight()
        elif random_enemy_move == 1:
            enemy_game[0].enemyLeft()
        elif random_enemy_move == 2:
            enemy_game[0].enemyUp()
        elif random_enemy_move == 3:
            enemy_game[0].enemyDown()
        map_game.updateMapEnemy(enemy_game[0])

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

    enemy_counter_time += 1

    if enemy_counter_time > 10:
        enemy_counter_time = 0

    pygame.draw.rect(screen, WHITE_COLOR, (0,200,400,50))
    # Health
    pygame.draw.rect(screen, LIME_COLOR, (20,210,player_game.health,10))
    pygame.draw.rect(screen, GREEN_COLOR, (20+player_game.health,210,100-player_game.health,10))
    # Energy
    pygame.draw.rect(screen, BLUE_COLOR, (20,230,player_game.energy,10))
    pygame.draw.rect(screen, DARK_BLUE_COLOR, (20+player_game.energy,230,100-player_game.energy,10))

    pygame.display.update()