# game data module
import pygame
import math
import graphic
from graphic import *
import shape_data
from shape_data import *
import player_data
from player_data import *
class map(object):
    wall_list = None
    enemy_sprites = None
    def __init__(self, map_number=0):
        self.map_number = map_number
        #print(self.map_number)
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
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

  
class map1(map):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [#[0, 0, 20, 250, graphic.BL],
                 [0, 40, 30, 720, graphic.Y],
                 [1250, 0, 30, 720, graphic.Y],
                 #[1260, 350, 20, 0, graphic.BL],
                 [0, 30, 1250, 20, graphic.Y],
                 [20, 700, 1250, 20, graphic.Y],
                 [80, 80, 20, 400, graphic.Y],
                 [130, 80, 20, 300, graphic.BL],
                 [280, 80, 20, 100, graphic.BL],
                 [580, 80, 20, 200, graphic.BL],
                 [780, 80, 20, 500, graphic.BL],
                 [580, 180, 400, 20, graphic.BL],
                 [480, 380, 400, 20, graphic.BL],
                 [380, 380, 400, 20, graphic.BL],
                 [580, 680, 400, 20, graphic.BL],
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 

         