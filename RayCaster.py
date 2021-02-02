import pygame
from Settings import *
from Map import GAMEMAP
import math


def ray_casting(SCREEN, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xCord, yCord = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAXDEPTH):
            x = xCord + depth * cos_a
            y = yCord + depth * sin_a
            if (x//TILE * TILE, y//TILE*TILE) in GAMEMAP:
                depth *= math.cos(player_angle - cur_angle)
                if depth == 0:
                    break
                proj_Height = Pro_COEFF / depth
                colorShade = 255/(1+depth*depth*0.0002)
                newShadedColor = (colorShade, colorShade//3, colorShade//2)
                pygame.draw.rect(SCREEN, newShadedColor, (ray * SCALE,
                                                          HALF_HEIGHT - proj_Height/2, SCALE, proj_Height))
                break
        cur_angle += DELTA_ANGLE
