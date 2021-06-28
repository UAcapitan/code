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
ENEMY_MIDDLE_COLOR = [0, 135, 0]
BULLET_COLOR = [10,10,10]
BOSS_LVL_COLOR = [70,70,70]
BLOCK_BOSS_COLOR = [30,30,30]
BOSS_COLOR = [128, 10, 10]

game_over = False

menu = False

win = False

boss_lvl = 2

clock = pygame.time.Clock()

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((400,250))

pygame.display.set_caption('Game_Hero')

screen.fill(GREEN_COLOR)

pygame.display.update()

# p - player
# e - enemy
# b - bonus
# t - tree
# em - enemy middle
# bu - bullet

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

    def updateMapEnemyMiddle(self, enemy):
        self.map[enemy.last_y][enemy.last_x] = 0
        self.map[enemy.y][enemy.x] = 'em'

    def updateMapBonus(self, bonus):
        self.map[bonus.y][bonus.x] = 'b'

    def updateMapTree(self, tree):
        self.map[tree.y][tree.x] = 't'
    
    def updateMapBullet(self, b):
        self.map[b.y][b.x] = 'bu'

    def updateMapBoss(self, enemy):
        self.map[enemy.last_y][enemy.last_x] = 0
        self.map[enemy.y][enemy.x] = 'bo'

    def newMap(self):
        global enemy_game
        global bonus_game
        global tree_game
        global enemy_middle_game
        global bullet_game

        self.map = [
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
        enemy_middle_game = []
        bonus_game = []
        tree_game = []
        bullet_game = []

        map_game.create_objects()
        if player_game.lvl >= boss_lvl:
            map_game.newBossLvl()

    def create_objects(self):
        global enemy_game
        global map_game
        global bonus_game
        global tree_game

        if player_game.lvl < boss_lvl:

            for i in range(50):
                tree_game.append(TreeGame(random.randint(0,18), random.randint(0,8)))

            for t in tree_game:
                map_game.updateMapTree(t)

            j = 1

            if player_game.lvl > 10:
                j = 2
            
            if player_game.lvl > 25:
                j = 3

            for i in range(random.randint(0,j*3)):
                enemy_game.append(EnemyGame(random.randint(0,18), random.randint(0,8)))
            
            for e in enemy_game:
                map_game.updateMapEnemy(e)

            if player_game.lvl >= 25:
                if player_game.lvl >= 25:
                    j = 1
                elif player_game.lvl >= 40:
                    j = 2
                elif player_game.lvl >= 50:
                    j = 3

                for i in range(random.randint(0,j)):
                    enemy_middle_game.append(EnemyMiddleGame(random.randint(0,18), random.randint(0,8)))
                
                for e in enemy_game:
                    map_game.updateMapEnemyMiddle(e)

            for i in range(random.randint(0,5)):
                bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))

            for b in bonus_game:
                map_game.updateMapBonus(b)

    def create_blind_map(self):
        self.map = [
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
        
        for b in bonus_game:
            map_game.updateMapBonus(b)

    def newBossLvl(self):
        self.map = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,'t','t','t',0,0,0,0,'t','t',0,0,0,0,'t','t','t',0,0,0],
            [0,0,'t',0,0,0,0,0,0,'t','t',0,0,0,0,0,0,'t',0,0,0],
            [0,0,'t',0,0,'t','t','t','t','t','t','t','t','t','t',0,0,'t',0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,'t',0,0,'t','t','t','t','t','t','t','t','t','t',0,0,'t',0,0,0],
            [0,0,'t',0,0,0,0,0,0,'t','t',0,0,0,0,0,0,'t',0,0,0],
            [0,0,'t','t','t',0,0,0,0,'t','t',0,0,0,0,'t','t','t',0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.x = 0
        self.y = 0

        map_game.updateMapBoss(boss_game)

# Player
class PlayerGame(EntityInMap):
    def __init__(self):
        super().__init__(0,0)
        self.last_x = 0
        self.last_y = 0
        self.health = 100
        self.energy = 100
        self.lvl = 1
        self.exp = 0
        self.skills = []
        self.skills_pos = 0
        self.side = 'right'

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

    def upLvl(self):
        global boss_game
        if self.exp >= self.lvl * 100:
                self.exp -= self.lvl * 100
                self.lvl += 1
                if self.lvl % 5 == 0:
                    self.newSkill()
                if self.lvl >= boss_lvl:
                    boss_game = BossGame()
                    map_game.newMap()
    
    def newSkill(self):
        if len(self.skills) < 10:
            n = random.randint(0,len(skills)-1)
            player_game.skills.append(skills[n])
            del skills[n]

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

# Boss
class BossGame(EnemyGame):
    def __init__(self):
        super().__init__(10,4)
        self.health = 500
        self.last_x = self.x
        self.last_y = self.y

# Enemy middle
class EnemyMiddleGame(EnemyGame):
    pass

# Bonus
class BonusGame(EntityInMap):
    def __init__(self, x, y):
        super().__init__(x,y)

# Tree
class TreeGame(EntityInMap):
    def __init__(self,x,y):
        super().__init__(x,y)

# Bullet
class BulletGame(EntityInMap):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.side = player_game.side

# Skill standart class
class Skill:
    def __init__(self, name, energy, full_name, description):
        self.name = name
        self.energy = energy
        self.full_name = full_name
        self.description = description

    def use(self):
        pass

# Skills
class FreezingSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            try:
                for i in range(len(enemy_game)):
                    del enemy_game[i]
            except:
                pass
            player_game.exp += player_game.lvl * random.randint(1,10)
            player_game.upLvl()

class HpRegenSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            player_game.health = 100

class ExpUpSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            player_game.exp += player_game.lvl * 100
            player_game.upLvl()

class ClearMapSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            map_game.create_blind_map()

class TeleportSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            map_game.newMap()

class EnergyRegenSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            player_game.energy = 100

class BonusCreateSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            for i in range(random.randint(0,10)):
                bonus_game.append(BonusGame(random.randint(0,18), random.randint(0,8)))

            for b in bonus_game:
                map_game.updateMapBonus(b)

class AllRegenSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            player_game.health = 100
            player_game.energy = 100

class ShootSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            if player_game.side == 'right':
                bullet_game.append(BulletGame(player_game.x+1, player_game.y))
            elif player_game.side == 'left':
                bullet_game.append(BulletGame(player_game.x-1, player_game.y))
            elif player_game.side == 'up':
                bullet_game.append(BulletGame(player_game.x, player_game.y-1))
            elif player_game.side == 'down':
                bullet_game.append(BulletGame(player_game.x, player_game.y+1))
            map_game.updateMapBullet(bullet_game[-1])

class KickSkill(Skill):
    def use(self):
        if player_game.energy > self.energy:
            player_game.energy -= self.energy
            if player_game.side == 'right':
                map_game.map[player_game.y][player_game.x+1] = 0
                for i in range(len(enemy_game)):
                    try:
                        if enemy_game[i].x == player_game.x+1 and enemy_game[i].y == player_game.y:
                            del enemy_game[i]
                            player_game.exp += 100 * player_game.lvl
                            player_game.upLvl()
                    except:
                        pass
            elif player_game.side == 'left':
                map_game.map[player_game.y][player_game.x-1] = 0
                for i in range(len(enemy_game)):
                    try:
                        if enemy_game[i].x == player_game.x-1 and enemy_game[i].y == player_game.y:
                            del enemy_game[i]
                            player_game.exp += 100 * player_game.lvl
                            player_game.upLvl()
                    except:
                        pass
            elif player_game.side == 'up':
                map_game.map[player_game.y-1][player_game.x] = 0
                for i in range(len(enemy_game)):
                    try:
                        if enemy_game[i].x == player_game.x and enemy_game[i].y == player_game.y-1:
                            del enemy_game[i]
                            player_game.exp += 100 * player_game.lvl
                            player_game.upLvl()
                    except:
                        pass
            elif player_game.side == 'down':
                map_game.map[player_game.y+1][player_game.x] = 0
                for i in range(len(enemy_game)):
                    try:
                        if enemy_game[i].x == player_game.x and enemy_game[i].y == player_game.y+1:
                            del enemy_game[i]
                            player_game.exp += 100 * player_game.lvl
                            player_game.upLvl()
                    except:
                        pass
            map_game.updateMapBullet(bullet_game[-1])

# Objects
map_game = MapGame()
player_game = PlayerGame()
enemy_game = []
enemy_middle_game = []
bonus_game = []
tree_game = []
bullet_game = []
boss_game = None

map_game.create_objects()

skills = [
    FreezingSkill('Fr', 40, 'Freezing', 
    ['Freezes some enemies', 'Gives some experience for freezing']),
    HpRegenSkill('HP', 70, 'HP regeneration',
    ['Restores all health']),
    ExpUpSkill('Exp', 90, 'Experience up', 
    ['Gain experience for using']),
    ClearMapSkill('Cl', 90, 'Clear map',
    ['Clears the map of trees']),
    TeleportSkill('Tp', 20, 'Teleportation',
    ['The player teleports to', 'a random point']),
    EnergyRegenSkill('E R', 50, 'Energy regeneration',
    ['Restores all energy']),
    BonusCreateSkill('Bon', 90, 'Bonus',
    ['Creates additional bonuses', 'on the map']),
    AllRegenSkill('A R', 70, 'All regeneration',
    ['Regenerates full health', 'and energy at the same time']),
    ShootSkill('Sh', 20, 'Shoot',
    ['Allows you to shoot a bullet that','destroys everything in its path']),
    KickSkill('K', 10, 'Kick',
    ['Allows you to destroy everything','that is near the player'])
    ]

# Dialogs
start_dialogs_pos = 0
start_dialogs = [
    'Hi, hero! Press SPACE.',
    'I will briefly tell',
    'you how to survive here.',
    'It`s an endless forest.',
    'It`s full of',
    'everything here.',
    'But full of enemies',
    'Bonuse - blue,',
    'Enemy - red',
    'You have health.',
    'Health - green bar',
    'And, energy is a blue bar.',
    'Level up and good luck!',
    'Press the button `i`',
    'to view the abilities.',
    'The button `x` can',
    'activate the ability.',
    ''
]

# Counter for moves
enemy_counter_time = 0

hp_regen_timer = 0

energy_regen_timer = 0

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
                player_game.side = 'right'
            elif i.key == pygame.K_a:
                player_game.playerLeft()
                player_game.side = 'left'
            elif i.key == pygame.K_w:
                player_game.playerUp()
                player_game.side = 'up'
            elif i.key == pygame.K_s:
                player_game.playerDown()
                player_game.side = 'down'
            elif i.key == pygame.K_e:
                player_game.exp += 500
                player_game.upLvl()
            elif i.key == pygame.K_z:
                map_game.newMap()
            elif i.key == pygame.K_RETURN:
                if game_over:
                    exit()
            elif i.key == pygame.K_i:
                menu = True if not(menu) else False
            elif i.key == pygame.K_SPACE:
                if len(start_dialogs) > start_dialogs_pos + 1:
                    start_dialogs_pos += 1
            elif i.key == pygame.K_x:
                try:
                    player_game.skills[player_game.skills_pos].use()
                except:
                    pass
            # Skills buttons
            elif i.key == pygame.K_1:
                player_game.skills_pos = 0
            elif i.key == pygame.K_2:
                player_game.skills_pos = 1
            elif i.key == pygame.K_3:
                player_game.skills_pos = 2
            elif i.key == pygame.K_4:
                player_game.skills_pos = 3
            elif i.key == pygame.K_5:
                player_game.skills_pos = 4
            elif i.key == pygame.K_6:
                player_game.skills_pos = 5
            elif i.key == pygame.K_7:
                player_game.skills_pos = 6
            elif i.key == pygame.K_8:
                player_game.skills_pos = 7
            elif i.key == pygame.K_9:
                player_game.skills_pos = 8
            elif i.key == pygame.K_0:
                player_game.skills_pos = 9
            map_game.updateMapPlayer(player_game)

    # Moves enemy
    for e in enemy_game:
        if enemy_counter_time == 5:
            random_enemy_move = random.randint(0,4)
            if random_enemy_move == 0:
                e.enemyRight()
            elif random_enemy_move == 1:
                e.enemyLeft()
            elif random_enemy_move == 2:
                e.enemyUp()
            elif random_enemy_move == 3:
                e.enemyDown()
        map_game.updateMapEnemy(e)
    for e in enemy_middle_game:
        if enemy_counter_time == 5:
            random_enemy_move = random.randint(0,4)
            if random_enemy_move == 0:
                e.enemyRight()
            elif random_enemy_move == 1:
                e.enemyLeft()
            elif random_enemy_move == 2:
                e.enemyUp()
            elif random_enemy_move == 3:
                e.enemyDown()
        map_game.updateMapEnemyMiddle(e)

    if player_game.lvl >= boss_lvl:
        random_enemy_move = random.randint(0,4)
        if random_enemy_move == 0:
            boss_game.enemyRight()
        elif random_enemy_move == 1:
            boss_game.enemyLeft()
        elif random_enemy_move == 2:
            boss_game.enemyUp()
        elif random_enemy_move == 3:
            boss_game.enemyDown()
        map_game.updateMapBoss(boss_game)

    try:
        for i in range(len(enemy_game)):
            if enemy_game[i].x == player_game.x and enemy_game[i].y == player_game.y:
                player_game.health -= random.randrange(10,50,10)
                if player_game.energy > 10:
                    player_game.energy -= 20
                    player_game.exp += 20 * player_game.lvl
                    player_game.upLvl()
                    del enemy_game[i]

        for i in range(len(enemy_middle_game)):
            if enemy_middle_game[i].x == player_game.x and enemy_middle_game[i].y == player_game.y:
                player_game.health -= random.randrange(50,90,10)
                if player_game.energy >= 50:
                    player_game.energy -= 50
                    player_game.exp += 50 * player_game.lvl
                    player_game.upLvl()
                    del enemy_middle_game[i]

        for i in range(len(bonus_game)):
            if bonus_game[i].x == player_game.x and bonus_game[i].y == player_game.y:
                player_game.exp += random.randint(1,25) * player_game.lvl
                player_game.upLvl()
                if player_game.energy < 100:
                    player_game.energy += 10
                player_game.upLvl()
                del bonus_game[i]

        for i in range(len(bullet_game)):
            try:
                if bullet_game[i].y < 0 or bullet_game[i].x < 0:
                    del bullet_game[i]
                    map_game.map[bullet_game[i].y][bullet_game[i].x] = 0
                else:
                    map_game.map[bullet_game[i].y][bullet_game[i].x] = 0
                    if bullet_game[i].side == 'right':
                        bullet_game[i].x += 1
                    elif bullet_game[i].side == 'left':
                        bullet_game[i].x -= 1
                    elif bullet_game[i].side == 'up':
                        bullet_game[i].y -= 1
                    elif bullet_game[i].side == 'down':
                        bullet_game[i].y += 1
                    map_game.updateMapBullet(bullet_game[i])
            except:
                del bullet_game[i]
            
        for i in range(len(bullet_game)):
            for b in range(len(enemy_game)):
                if bullet_game[i].x == enemy_game[b].x and bullet_game[i].y == enemy_game[b].y:
                    map_game.map[bullet_game[i].y][bullet_game[i].x] = 0
                    del bullet_game[i]
                    del enemy_game[i]
                    player_game.exp += 70 * player_game.lvl
                    player_game.upLvl()
            for b in range(len(bonus_game)):
                if bullet_game[i].x == bonus_game[b].x and bullet_game[i].y == bonus_game[b].y:
                    map_game.map[bullet_game[i].y][bullet_game[i].x] = 'bu'
                    del bonus_game[i]
    except:
        pass    
 
    # Color map
    if player_game.lvl < boss_lvl:
        screen.fill(GREEN_COLOR)
    else:
        screen.fill(BOSS_LVL_COLOR)

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
                if player_game.lvl < boss_lvl:
                    pygame.draw.rect(screen, DARK_GREEN_COLOR, (map_game.x,map_game.y,20,20))
                else:
                    pygame.draw.rect(screen, BLOCK_BOSS_COLOR, (map_game.x,map_game.y,20,20))
            if j == 'em':
                pygame.draw.rect(screen, ENEMY_MIDDLE_COLOR, (map_game.x,map_game.y,20,20))
            if j == 'bu':
                pygame.draw.rect(screen, BULLET_COLOR, (map_game.x,map_game.y,20,20))
            if j == 'bo':
                pygame.draw.rect(screen, BOSS_COLOR, (map_game.x,map_game.y,20,20))
            map_game.x += 20
        map_game.x = 0
        map_game.y += 20
    
    map_game.y = 0

    # Enemy speed
    enemy_counter_time += 1

    if enemy_counter_time > 5:
        enemy_counter_time = 0

    # Hp regen
    hp_regen_timer += 1

    if hp_regen_timer > 100:
        hp_regen_timer = 0
        if player_game.health < 100 and not game_over:
            player_game.health += 10

    # Energy regen
    energy_regen_timer += 1

    if energy_regen_timer > 80:
        energy_regen_timer = 0
        if player_game.energy < 100 and not game_over:
            player_game.energy += 10

    # Scales
    pygame.draw.rect(screen, WHITE_COLOR, (0,200,400,50))

    # Health
    pygame.draw.rect(screen, LIME_COLOR, (20,210,player_game.health,10))
    pygame.draw.rect(screen, GREEN_COLOR, (20+player_game.health,210,100-player_game.health,10))

    # Energy
    pygame.draw.rect(screen, BLUE_COLOR, (20,230,player_game.energy,10))
    pygame.draw.rect(screen, DARK_BLUE_COLOR, (20+player_game.energy,230,100-player_game.energy,10))

    # Lvl
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    textsurface = myfont.render(str(player_game.lvl) + ' lvl', False, (0, 0, 0))
    screen.blit(textsurface,(150, 205))

    # Exp
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    textsurface = myfont.render(str(player_game.exp) + ' / ' + str(player_game.lvl * 100) + ' exp', False, (0, 0, 0))
    screen.blit(textsurface,(150, 225))

    # Dialog
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render(start_dialogs[start_dialogs_pos], False, (0, 0, 0))
    screen.blit(textsurface,(210, 205))

    # Menu
    if menu:

        screen.fill(WHITE_COLOR)

        myfont = pygame.font.SysFont('Arial', 20)
        textsurface = myfont.render('Skills', False, (0, 0, 0))
        screen.blit(textsurface,(29, 5))

        myfont = pygame.font.SysFont('Comic Sans MS', 10)

        if player_game.skills_pos < 5:
            pygame.draw.rect(screen, BLUE_COLOR, (28+player_game.skills_pos*35,28,34,34))
        else:
            pygame.draw.rect(screen, BLUE_COLOR, (28+(player_game.skills_pos-5)*35,68,34,34))
            
        for i in range(0,5):
            pygame.draw.rect(screen, LIME_COLOR, (30+i*35,30,30,30))
            textsurface = myfont.render(str(i+1), False, (0, 0, 0))
            screen.blit(textsurface,(31+i*35, 47))

        for i in range(0,5):
            pygame.draw.rect(screen, LIME_COLOR, (30+i*35,70,30,30))
            textsurface = myfont.render(str(i+6), False, (0, 0, 0))
            screen.blit(textsurface,(31+i*35, 87))
        
        myfont = pygame.font.SysFont('Comic Sans MS', 15)

        for i in range(len(player_game.skills)):
            textsurface = myfont.render(player_game.skills[i].name, False, (0, 0, 0))
            if i < 5:
                screen.blit(textsurface,(35+i*35, 30))
            else:
                screen.blit(textsurface,(35+(i-5)*35, 70))

        try:
            name = player_game.skills[player_game.skills_pos].full_name
            en = player_game.skills[player_game.skills_pos].energy
            description = player_game.skills[player_game.skills_pos].description
        except:
            name = ''
            en = ''
            description = ''
        
        textsurface = myfont.render('Name: ' + name, False, (0, 0, 0))
        screen.blit(textsurface,(30, 110))
        textsurface = myfont.render('Need energy: ' + str(en), False, (0, 0, 0))
        screen.blit(textsurface,(30, 130))
        textsurface = myfont.render('Description: ', False, (0, 0, 0))
        screen.blit(textsurface,(30, 150))
        for i in range(len(description)):
            textsurface = myfont.render(description[i], False, (0, 0, 0))
            screen.blit(textsurface,(30, 180+i*20))

    # Game over
    if player_game.health <= 0:
        screen.fill(GREEN_COLOR)
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('Game Over', False, (255, 255, 255))
        screen.blit(textsurface,(70,70))
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        textsurface = myfont.render('Press Enter for quit', False, (255, 255, 255))
        screen.blit(textsurface,(130,150))
        game_over = True

    if win:
        screen.fill(GREEN_COLOR)
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        textsurface = myfont.render('You won the game', False, (255, 255, 255))
        screen.blit(textsurface,(70,70))
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        textsurface = myfont.render('Press Enter for quit', False, (255, 255, 255))
        screen.blit(textsurface,(130,150))
        game_over = True

    # Update display
    pygame.display.update()