import math
import pygame
import graphic
from graphic import *
import player_data 
from player_data import *


pygame.init()

set_screen_size = (1280, 720)
set_screen(set_screen_size,screen)


done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(W)
    font = pygame.font.Font(None, 30)
    text = font.render("TESTING GAME",True,BL)
    screen.blit(text,[0,0])
    # --- Drawing code should go here
    map_selection = 2
    running_map = map(map_selection)
    map.draw_map(running_map)
   
    #display update
    pygame.display.flip()

    #FPS contral
    clock.tick(60)

# Close the window and quit.
pygame.quit()
                       