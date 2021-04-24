import pygame

pygame.init()

map = []

while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()