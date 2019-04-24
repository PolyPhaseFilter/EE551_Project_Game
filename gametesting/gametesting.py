import math
import pygame
import graphic
from graphic import *
import player_data 
from player_data import *
import shape
from shape import *

pygame.init()

set_screen_size = (1280, 720)
set_screen(set_screen_size,screen)


done = False

clock = pygame.time.Clock()
# Speed in pixels per frame
player_one.movement_speed_x=0
player_one.movement_speed_y=0
player_two.movement_speed_x=0
player_two.movement_speed_y=0
#set location
player_one.location_x=0
player_one.location_y=0
player_two.location_x=0
player_two.location_y=0
i=0
# -------- Main Program Loop -----------
while not done:
   
    predetor = graphic.R
    if i <= 60*20:
        predetor = graphic.R
    else:
        predetor = graphic.B
        if i == 60*40:
            i = 0
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif  event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_a:
                player_one.movement_speed_x = -3
            elif event.key == pygame.K_d:
                player_one.movement_speed_x = 3
            elif event.key == pygame.K_w:
                player_one.movement_speed_y = -3
            elif event.key == pygame.K_s:
                player_one.movement_speed_y = 3

        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_one.movement_speed_x  = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                player_one.movement_speed_y = 0
#player two
    if  event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_two.movement_speed_x = -3
        elif event.key == pygame.K_RIGHT:
            player_two.movement_speed_x = 3
        elif event.key == pygame.K_UP:
            player_two.movement_speed_y = -3
        elif event.key == pygame.K_DOWN:
            player_two.movement_speed_y = 3

    elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_two.movement_speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_two.movement_speed_y = 0
    # --- Game logic should go here
    player_one.location_x += player_one.movement_speed_x
    player_one.location_y += player_one.movement_speed_y
    player_two.location_x += player_two.movement_speed_x
    player_two.location_y += player_two.movement_speed_y
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
    running_map = map.map(map_selection)
    map.map.draw_map(running_map)
    # --- Drawing character
    player_one.color=graphic.B
    player_two.color=graphic.R
    #draw character
    shape.predetor_sign(screen,predetor,550,50)
    shape.draw_character_one(screen,player_one.location_x,player_one.location_y)
    shape.draw_character_two(screen,player_two.location_x,player_two.location_y)
    #display update
    pygame.display.flip()
    
    #FPS contral
    i += 1
    i
    clock.tick(60)

# Close the window and quit.
pygame.quit()
                       