# player data module
import pygame
from pygame import *
import graphic
from graphic import *
class Player():
    def __init__(self, life_points=100, atk_power=10, atk_range=0, atk_speed=1.0, ult_range=0, ult_style=0
                 , ult_cool_down=0, movement_speed_x=0, movement_speed_y=0 , color = (0,0,0)
                 ,box=[20,20],location_x=0,location_y=0,direction=(0,0)):
        self.life_Points = life_points
        self.atk_Power = atk_power
        self.atk_range = atk_range
        self.ult_range = ult_range
        self.atk_speed = atk_speed
        self.ult_style = ult_style
        self.movement_speed_x = movement_speed_x
        self.movement_speed_y = movement_speed_y
        self.location_x=location_x
        self.location_y=location_y
        self.ult_cool_down = ult_cool_down
        self.color=color
        self.box=box
        self.direction=direction
        
    def isAlive(self):
        return self.life_points > 0

    def takeHit(self, atk_power=0):
        self.life_points -= atk_power

player_one = Player()
player_two = Player()

class Blue_player_hitbox(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self, x , y):
        super().__init__()

        self.image=pygame.Surface([14,14])
        self.image.fill(graphic.B)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
       # player_one.life_points -= player_two.atk_power


class Red_player_hitbox(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self,x , y):
        super().__init__()

        self.image=pygame.Surface([14,14])
        self.image.fill(graphic.R)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



