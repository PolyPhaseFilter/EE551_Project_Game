# game data module
import pygame
import math
import graphic
from graphic import *

class map():
    def __init__(self, map_number=0):
        self.map_number = map_number
        #print(self.map_number)

    def draw_map(self):
        #print(self.map_number)
        if self.map_number == 0:
            print("no map selected")
        elif self.map_number == 1:
            self.draw_map_one()
        else:
            print("no such map")
    
    def draw_map_one(self):
        #print(graphic.screen)
        for i in range(2000):
            radians_x = i / 20
            radians_y = i / 6
            x = int(75 * math.sin(radians_x)) + 500
            y = int(75 * math.cos(radians_y)) + 500
        #for i in range(1280):

            pygame.draw.line(graphic.screen, graphic.BL, [x, y], [x+5, y], 5)