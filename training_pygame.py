import pygame
import sys

# Каркас игры на Pygame
# pygame.init()
# pygame.display.set_mode((600,400))

# FPS = 60

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     clock.tick(FPS)

# Задание

# pygame.init()
# pygame.display.set_mode((600,400))

# FPS = 60

# clock = pygame.time.Clock()

# while True:
#     pygame.display.set_caption('Pygame')
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     clock.tick(FPS)

# Модуль pygame.draw

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     surface_main.fill(WHITE)
#     pygame.draw.circle(surface_main, ORANGE, (x,y), r)
#     pygame.display.update()
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# Задание

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     surface_main.fill(WHITE)
#     pygame.draw.rect(surface_main, ORANGE, (x, y, r, r))
#     pygame.display.update()
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# События клавиатуры

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif i.type == pygame.KEYUP:
#             reverse_move = True
#     surface_main.fill(WHITE)
#     pygame.draw.rect(surface_main, ORANGE, (x, y, r, r))
#     pygame.display.update()
#     if x > 0 and reverse_move:
#         x -= 4
#     elif x <= 0:
#         reverse_move = False
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# События мыши

# pygame.init()

# WIDTH = 600
# HEIGHT = 400
# FPS = 60
# MOVING_CIRCLE = False
# y = 400
# y_mouse = 0
# BOOM = False
# WHITE = (255,255,255)
# ORANGE = (255, 150, 100)
# BOOM_RESULT = False

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif i.type == pygame.MOUSEBUTTONDOWN:
#             y_mouse = pygame.mouse.get_pos()[1]
#             MOVING_CIRCLE = True

#     if MOVING_CIRCLE and BOOM_RESULT:
#         y = 400
#         BOOM = False
#         BOOM_RESULT = False

#     surface_main.fill(WHITE)
#     if not BOOM:
#         pygame.draw.circle(surface_main, ORANGE, (300, y), 10)
#     else:
#         pygame.draw.rect(surface_main, ORANGE, (290, y-10, 20, 20))
#         BOOM_RESULT = True
#     pygame.display.update()
     
#     if MOVING_CIRCLE and y > y_mouse:
#         y -= 2
#     elif MOVING_CIRCLE and y <= y_mouse:
#         MOVING_CIRCLE = False
#         BOOM = True

#     clock.tick(FPS)

# Класс Surface и метод blit()

# pygame.init()

# WIDTH = 600
# HEIGHT = 400
# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# x = 0

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# surface_main.fill(WHITE)

# surface_2 = pygame.Surface((WIDTH / 6, HEIGHT))
# surface_2.fill(WHITE)

# pygame.draw.rect(surface_2, ORANGE, (10,10, 80, 80))
# pygame.draw.circle(surface_2, ORANGE, (50, 150), 40)
# pygame.draw.polygon(surface_2, ORANGE, ((50, 210), (90, 270), (10, 270)))

# surface_main.blit(surface_2, (x,0))

# pygame.display.update()

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
    
#     if x > 600:
#         x = -90

#     surface_main.blit(surface_2, (x,0))

#     pygame.display.update()

#     x += 1
    
#     clock.tick(FPS)