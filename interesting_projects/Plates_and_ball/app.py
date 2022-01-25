import pygame as pg
import random
import time
import sys

pg.init()
pg.font.init()


COLORS = {
    'white': (255,255,255),
    'black': (0,0,0)
}

SIZE_ROOT = {
    'x':700,
    'y':400
}

SOUNDS = {
    'hit': pg.mixer.Sound('sounds/Blip_Select.ogg'),
    'border': pg.mixer.Sound('sounds/Blip_Select5.ogg'),
    'goal': pg.mixer.Sound('sounds/Blip_Select12.ogg'),
    'win': pg.mixer.Sound('sounds/Blip_Select15.ogg')
}


class Game:
    def __init__(self):
        pg.display.set_caption('Plates and Ball')
        self.root = pg.display.set_mode((SIZE_ROOT['x'],SIZE_ROOT['y']))
        self.clock = pg.time.Clock()
        self.work = True
        self.game_run = True
        self.setSpeedAndHits()

        self.plate_left = Plate(COLORS['white'], 10, 30)
        self.plate_right = Plate(COLORS['black'], SIZE_ROOT['x']-20, 30)
        self.ball = Ball(SIZE_ROOT['x']/2-20, SIZE_ROOT['y']/2-10, COLORS['white'])

        self.points = {
            'left': 0,
            'right': 0
        }

        self.myfont = pg.font.SysFont('Comic Sans MS', 50)

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.plate_left)
        self.all_sprites.add(self.plate_right)
        self.all_sprites.add(self.ball)

        self.run()

    def run(self):
        while True:
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                            self.pause()
            if self.work:

                self.checkKeys()

                self.bgScreen()

                self.pointsShow()

                self.ball.move(self.speed)
                self.hitTheBall()
                self.checkGoal()
                self.ball.draw()

                self.all_sprites.update()

                self.all_sprites.draw(self.root)

                pg.display.flip()

                self.clock.tick(60)

    def bgScreen(self):
        self.root.fill(COLORS['black'])
        pg.draw.rect(self.root, COLORS['white'], [SIZE_ROOT['x']/2, 0, SIZE_ROOT['x']/2, SIZE_ROOT['y']])

    def checkKeys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.plate_left.rect.top >= 10:
            self.plate_left.moveUp()
        if keys[pg.K_s] and self.plate_left.rect.bottom <= SIZE_ROOT['y'] - 10:
            self.plate_left.moveDown()
        if keys[pg.K_UP] and self.plate_right.rect.top >= 10:
            self.plate_right.moveUp()
        if keys[pg.K_DOWN] and self.plate_right.rect.bottom <= SIZE_ROOT['y'] - 10:
            self.plate_right.moveDown()

    def hitTheBall(self):
        if self.plate_left.rect.left >= self.ball.rect.left <= self.plate_left.rect.right:
            if self.plate_left.rect.top <= self.ball.rect.center[1] <= self.plate_left.rect.bottom:
                self.ball.setDirection(1, self.ball.direction_y)
                self.addHits()

        if self.plate_right.rect.left <= self.ball.rect.right >= self.plate_right.rect.right:
            if self.plate_right.rect.top <= self.ball.rect.center[1] <= self.plate_right.rect.bottom:
                self.ball.setDirection(0, self.ball.direction_y)
                self.addHits()

    def checkGoal(self):
        if self.ball.rect.left <= 0:
            self.work = False
            self.addPoint('right')
        if self.ball.rect.right >= SIZE_ROOT['x']:
            self.work = False
            self.addPoint('left')
        if self.ball.rect.left <= 0 or self.ball.rect.right >= SIZE_ROOT['x']:
            self.ifGoal()

    def ifGoal(self):
        SOUNDS['goal'].play()
        self.setSpeedAndHits()
        self.showRoundScore()
        self.myfont = pg.font.SysFont('Comic Sans MS', 50)
        time.sleep(1)
        self.ball.rect.x = SIZE_ROOT['x']/2-20
        self.ball.rect.y = random.randint(20, SIZE_ROOT['y']-20)
        self.ball.setDirection(random.randint(0,1),random.randint(0,1))
        self.work = True
        
    def addPoint(self, p):
        self.points[p] += 1
        self.win()

    def win(self):
        if self.points['left'] == 15 or self.points['right'] == 15:
            SOUNDS['win'].play()
            self.bgScreen()
            pg.display.flip()
        if self.points['left'] == 15:
            left = self.myfont.render('Left', False, COLORS['white'])
            win = self.myfont.render('win!', False, COLORS['black'])
            self.root.blit(left,(125,120))
            self.root.blit(win,(SIZE_ROOT['x']/2+135,190))
            pg.display.flip()
        if self.points['right'] == 15:
            right = self.myfont.render('Right', False, COLORS['black'])
            win = self.myfont.render('win!', False, COLORS['white'])
            self.root.blit(right,(SIZE_ROOT['x']/2+120,120))
            self.root.blit(win,(130,190))
            pg.display.flip()
        if self.points['left'] == 15 or self.points['right'] == 15:
            time.sleep(1)
            self.game_run = False

    def pointsShow(self):
        left = self.myfont.render(str(self.points['left']), False, COLORS['white'])
        right = self.myfont.render(str(self.points['right']), False, COLORS['black'])
        self.root.blit(left,(SIZE_ROOT['x']/2-60,10))
        self.root.blit(right,(SIZE_ROOT['x']/2+30,10))

    def addSpeed(self):
        self.speed += 1

    def addHits(self):
        SOUNDS['hit'].play()
        self.hits += 1
        if self.hits == 10:
            self.addSpeed()
        if self.hits == 20:
            self.addSpeed()
        if self.hits == 30:
            self.addSpeed()
        if self.hits == 50:
            self.addSpeed()
        
    def setSpeedAndHits(self):
        self.speed = 3
        self.hits = 0

    def showRoundScore(self):
        self.bgScreen()
        self.myfont = pg.font.SysFont('Comic Sans MS', 120)
        left = self.myfont.render(str(self.points['left']), False, COLORS['white'])
        right = self.myfont.render(str(self.points['right']), False, COLORS['black'])
        if self.points['left'] < 10:
            self.root.blit(left,(SIZE_ROOT['x']/2-210,90))
        else:
            self.root.blit(left,(SIZE_ROOT['x']/2-230,90))
        if self.points['right'] < 10:
            self.root.blit(right,(SIZE_ROOT['x']/2+150,90))
        else:
            self.root.blit(right,(SIZE_ROOT['x']/2+130,90))
        pg.display.flip()

    def pause(self):
        if self.work:
            self.pauseText()
            self.work = False
        else:
            self.work = True

    def pauseText(self):
        self.bgScreen()
        text_1 = self.myfont.render('Pause', False, COLORS['white'])
        self.root.blit(text_1,(SIZE_ROOT['x']/2-250,150))
        text_2 = self.myfont.render('Pause', False, COLORS['black'])
        self.root.blit(text_2,(SIZE_ROOT['x']/2+120,150))
        pg.display.flip()


class Plate(pg.sprite.Sprite):
    def __init__(self, color, x, y):

        super().__init__()

        self.image = pg.Surface((10,70))
        self.image.fill(color)

        self.draw(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def moveUp(self):
        self.rect.y -= 10

    def moveDown(self):
        self.rect.y += 10

    def draw(self, color):
        pg.draw.rect(self.image, color, [0,0,10,50])


class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, color):

        super().__init__()

        self.image = pg.Surface((20,20), pg.SRCALPHA, 32)

        self.color = color

        # Directions
        # 0 - Left, Down
        # 1 - Right, Up
        self.setDirection(random.randint(0,1),random.randint(0,1))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(20, SIZE_ROOT['y']-20)

    def setDirection(self, x, y):
        self.direction_x = x
        self.direction_y = y

    def move(self, speed):
        self.checkDirection()
        if self.direction_x == 0:
            self.rect.x -= speed
        if self.direction_y == 0:
            self.rect.y += speed
        if self.direction_x == 1:
            self.rect.x += speed
        if self.direction_y == 1:
            self.rect.y -= speed
        self.changeColor()

    def checkDirection(self):
        if self.rect.top <= 3:
            SOUNDS['border'].play()
            self.setDirection(self.direction_x, 0)
        if self.rect.bottom >= SIZE_ROOT['y'] - 3:
            SOUNDS['border'].play()
            self.setDirection(self.direction_x, 1)

    def changeColor(self):
        if self.rect.center[0] < SIZE_ROOT['x']/2:
            self.color = COLORS['white']
        else:
            self.color = COLORS['black']

    def draw(self):
        pg.draw.circle(self.image, self.color, [10, 10], 10, 0)


if __name__ == '__main__':
    game = Game()