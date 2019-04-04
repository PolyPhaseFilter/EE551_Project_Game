
import pygame
import player_data
from player_data import *

BL = (0, 0, 0)
W = (255, 255, 255)
G = (0, 255, 0)
R = (255, 0, 0)
B = (0, 0, 255)

pygame.init()

set_screen_size = (1280, 720)
set_screen = pygame.display.set_mode(set_screen_size)
pygame.display.set_caption("HAHAHAHA")

done = False