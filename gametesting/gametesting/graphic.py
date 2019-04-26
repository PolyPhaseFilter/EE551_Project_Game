
import pygame
import map
from map import *
import player_data
from player_data import *

BL = (0, 0, 0)
W = (255, 255, 255)
G = (0, 255, 0)
R = (255, 0, 0)
Y = (180,180,100)
B = (0, 0, 255)
B_ATK = (1, 1, 255)
R_ATK = (255, 1, 1)

screen =pygame.display.set_mode((0,0))


def set_screen(set_screen_size, screen):
    screen= pygame.display.set_mode(set_screen_size)
    pygame.display.set_caption("HAHAHAHA")

   