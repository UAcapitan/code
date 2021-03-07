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

# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     pygame.display.set_caption('Pygame')
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