# --------------------------------------
# Development start date: 24 Apr 2021
# --------------------------------------

import pygame
import sys
import random

FPS = 10
GREEN_COLOR = [0, 128, 0]
DARK_GREEN_COLOR = [0, 64, 0]
LIME_COLOR = [0,255,0]
RED_COLOR = [255,0,0]
DARK_BLUE_COLOR = [0,0,128]
BLUE_COLOR = [0,0,255]
WHITE_COLOR = [230,230,230]

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400,250))

pygame.display.set_caption('Game_Hero')

screen.fill(GREEN_COLOR)

pygame.display.update()

# p - player
# e - enemy
# b - bonus
# t - tree


# Standart entity
class EntityInMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Map
class MapGame:
    def __init__(self):
        self.map = [
            ['p',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.x = 0
        self.y = 0

    def updateMapPlayer(self, player):
        self.map[player.last_y][player.last_x] = 0
        self.map[player.y][player.x] = 'p'

    def updateMapEnemy(self, enemy):
        self.map[enemy.last_y][enemy.last_x] = 0
        self.map[enemy.y][enemy.x] = 'e'

    def updateMapBonus(self, bonus):
        self.map[bonus.y][bonus.x] = 'b'

    def updateMapTree(self, tree):
        self.map[tree.y][tree.x] = 't'

    def newMap(self):
        global enemy_game
        global bonus_game
        global tree_game

        self.map = self.map = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.x = 0
        self.y = 0

        enemy_game = []
        bonus_game = []
        tree_game = []

        map_game.create_objects()

    def create_objects(self):
        global enemy_game
        global map_game
        global bonus_game
        global tree_game

        enemy_game.append(EnemyGame(random.randint(0,18), random.randint(0,8)))
        map_game.updateMapEnemy(enemy_game[0])

        bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))
        bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))
        bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))

        for b in bonus_game:
            map_game.updateMapBonus(b)

        for i in range(50):
            tree_game.append(TreeGame(random.randint(0,18), random.randint(0,8)))

        for t in tree_game:
            map_game.updateMapTree(t)

# Player
class PlayerGame(EntityInMap):
    def __init__(self):
        super().__init__(0,0)
        self.last_x = 0
        self.last_y = 0
        self.health = 100
        self.energy = 100

    def playerRight(self):
        if not(map_game.map[self.y][self.x+1] == 't'):
            if self.x <= 18:
                self.x += 1
                self.last_x = self.x - 1
                self.last_y = self.y
            else:
                self.x = 0
                map_game.newMap()

    def playerLeft(self):
        if not(map_game.map[self.y][self.x-1] == 't'):
            if self.x > 0:
                self.x -= 1
                self.last_x = self.x + 1
                self.last_y = self.y
            else:
                self.x = 19
                map_game.newMap()

    def playerUp(self):
        if not(map_game.map[self.y-1][self.x] == 't'):
            if self.y > 0:
                self.y -= 1
                self.last_y = self.y + 1
                self.last_x = self.x
            else:
                self.y = 9
                map_game.newMap()

    def playerDown(self):
        if not(map_game.map[self.y+1][self.x] == 't'):
            if self.y <= 8:
                self.y += 1
                self.last_y = self.y - 1
                self.last_x = self.x
            else:
                self.y = 0
                map_game.newMap()

    def damagePlayer(self, hp):
        self.health -= hp
        if self.health < 0:
            self.health = 0

    def useEnergyPlayer(self, en):
        self.energy -= en
        if self.energy < 0:
            self.energy = 0

# Enemy
class EnemyGame(EntityInMap):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.last_x = x
        self.last_y = y

    def enemyRight(self):
        if not(map_game.map[self.y][self.x+1] == 't'):
            if self.x <= 18:
                self.x += 1
                self.last_x = self.x - 1
                self.last_y = self.y

    def enemyLeft(self):
        if not(map_game.map[self.y][self.x-1] == 't'):
            if self.x > 0:
                self.x -= 1
                self.last_x = self.x + 1
                self.last_y = self.y

    def enemyUp(self):
        if not(map_game.map[self.y-1][self.x] == 't'):
            if self.y > 0:
                self.y -= 1
                self.last_y = self.y + 1
                self.last_x = self.x

    def enemyDown(self):
        if not(map_game.map[self.y+1][self.x] == 't'):
            if self.y <= 8:
                self.y += 1
                self.last_y = self.y - 1
                self.last_x = self.x

# Bonus
class BonusGame(EntityInMap):
    def __init__(self, x, y):
        super().__init__(x,y)

# Tree
class TreeGame(EntityInMap):
    def __init__(self,x,y):
        super().__init__(x,y)

# Objects
map_game = MapGame()
player_game = PlayerGame()
enemy_game = []
bonus_game = []
tree_game = []

map_game.create_objects()

# Counter for moves
enemy_counter_time = 0

while True:

    # FPS
    clock.tick(FPS)

    # Game events
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
            elif i.key == pygame.K_z:
                map_game.newMap()
            map_game.updateMapPlayer(player_game)

    # Moves enemy
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

    # Color map
    screen.fill(GREEN_COLOR)

    # Draw entities
    for i in map_game.map:
        for j in i:
            if j == 'p':
                pygame.draw.rect(screen, LIME_COLOR, (map_game.x,map_game.y,20,20))
            if j == 'e':
                pygame.draw.rect(screen, RED_COLOR, (map_game.x,map_game.y,20,20))
            if j == 'b':
                pygame.draw.rect(screen, BLUE_COLOR, (map_game.x,map_game.y,20,20))
            if j == 't':
                pygame.draw.rect(screen, DARK_GREEN_COLOR, (map_game.x,map_game.y,20,20))
            map_game.x += 20
        map_game.x = 0
        map_game.y += 20
    
    map_game.y = 0

    enemy_counter_time += 1

    if enemy_counter_time > 10:
        enemy_counter_time = 0

    # Scales
    pygame.draw.rect(screen, WHITE_COLOR, (0,200,400,50))
    # Health
    pygame.draw.rect(screen, LIME_COLOR, (20,210,player_game.health,10))
    pygame.draw.rect(screen, GREEN_COLOR, (20+player_game.health,210,100-player_game.health,10))
    # Energy
    pygame.draw.rect(screen, BLUE_COLOR, (20,230,player_game.energy,10))
    pygame.draw.rect(screen, DARK_BLUE_COLOR, (20+player_game.energy,230,100-player_game.energy,10))

    # Update display
    pygame.display.update()