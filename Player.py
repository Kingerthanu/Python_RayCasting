from Settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    def move(self):
        SIN_a = math.sin(self.angle)
        COS_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * COS_a
            self.y += player_speed * SIN_a
        if keys[pygame.K_s]:
            self.x += -player_speed * COS_a
            self.y += -player_speed * SIN_a
        if keys[pygame.K_a]:
            self.x += player_speed * SIN_a
            self.y += -player_speed * COS_a
        if keys[pygame.K_d]:
            self.x += -player_speed * SIN_a
            self.y += player_speed * COS_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def pos(self):
        return (self.x, self.y)
