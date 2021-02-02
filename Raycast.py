import numpy as np
from Settings import *
import pygame
from Player import Player
from Map import GAMEMAP
from RayCaster import ray_casting

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
GameClock = pygame.time.Clock()
player = Player()
while True:
    SCREEN.fill(pygame.Color("Black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.move()
    pygame.draw.rect(SCREEN, pygame.Color("Blue"), (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(SCREEN, pygame.Color("Grey"),
                     (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    ray_casting(SCREEN, player.pos(), player.angle)
    pygame.display.flip()
