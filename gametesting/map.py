# game data module
import pygame
import math
import graphic
from graphic import *
import shape_data
from shape_data import *
import player_data
from player_data import *
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
        elif self.map_number == 2:
            self.draw_map_two()
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

    def draw_map_two(self):
        #border
        for i in (20,710):
            pygame.draw.line(graphic.screen, graphic.BL, [0, i], [1280,i], 5)
        for i in (10,1270):
            pygame.draw.line(graphic.screen, graphic.BL, [i, 20], [i,720], 5)

        #map core
        for i in range (20,710, 80):
            pygame.draw.line(graphic.screen, graphic.BL, [80, i], [400,i], 5)

        for i in range (20,710, 80):
            pygame.draw.line(graphic.screen, graphic.BL, [800, i], [1190,i], 5)
           
        for i in range (0,4):
            pygame.draw.line(graphic.screen, graphic.BL, [80, 100+2*i*80], [80,180+2*i*80], 5)
            pygame.draw.line(graphic.screen, graphic.BL, [1190, 100+2*i*80], [1190,180+2*i*80], 5)
        for i in range (0,3):    
            pygame.draw.line(graphic.screen, graphic.BL, [400, 180+2*i*80], [400,260+2*i*80], 5)
            pygame.draw.line(graphic.screen, graphic.BL, [800, 180+2*i*80], [800,260+2*i*80], 5)

  


        