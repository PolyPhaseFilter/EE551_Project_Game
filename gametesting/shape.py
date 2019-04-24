import pygame
import math
import graphic
from graphic import *
import shape_data
from shape_data import *
import player_data
from player_data import *

def draw_character_one(screen,x,y):
     pygame.draw.ellipse(screen, B, [x, y, 20, 20], 0)

def draw_character_two(screen,x,y):
     pygame.draw.ellipse(screen, R, [x, y, 20, 20], 0)

def predetor_sign(screen,color,x,y):
     pygame.draw.ellipse(screen, color, [x, y, 30, 30], 0)


class Blue_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4,9])
        self.image.fill(B_ATK)
        self.rect = self.image.get_rect()
        

    def update(self):
        if player_one.direction == (0,0):
            self.rect.x -= 3
        elif player_one.direction == (1,1):
            self.rect.x += 3
        elif player_one.direction == (0,1):
            self.rect.y -= 3
        elif player_one.direction == (1,0):
            self.rect.y += 3

class Red_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4,9])
        self.image.fill(R_ATK)
        self.rect = self.image.get_rect()

    def update(self):
        if player_two.direction == (0,0):
            self.rect.x -= 3
        elif player_two.direction == (1,1):
            self.rect.x += 3
        elif player_two.direction == (0,1):
            self.rect.y -= 3
        elif player_two.direction == (1,0):
            self.rect.y += 3