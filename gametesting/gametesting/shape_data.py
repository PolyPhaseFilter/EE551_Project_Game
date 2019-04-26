import graphic
from graphic import *
import player_data
from player_data import *
import map
from map import *

#need fix
# tank mode, not yet designed........
class shape_tpye():
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, box):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([box[0], box[1]]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, box[0], box[1]))
 
        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)
 
        # Return the image
        return image

