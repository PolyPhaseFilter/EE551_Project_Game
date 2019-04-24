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