import math
import pygame
import graphic
from graphic import *
import player_data 
from player_data import *
import shape
from shape import *


def main():
    pygame.init()

    set_screen_size = (1280, 720)
    set_screen(set_screen_size,screen)
  
    #sprite++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    all_sprites_list = pygame.sprite.Group()
    # List of each bullet
    bullet_list = pygame.sprite.Group()
    player1_list = pygame.sprite.Group()
    player2_list = pygame.sprite.Group()
    done = False
     
    maps = []
 
    map = map1()
    maps.append(map)
 
    current_room_no = 0
    current_room = maps[current_room_no]
    clock = pygame.time.Clock()
    # Speed in pixels per frame
    #player_one.movement_speed_x=0
    #player_one.movement_speed_y=0
    #player_two.movement_speed_x=0
    #player_two.movement_speed_y=0
    #set location
    #player_one.location_x=40
    #player_one.location_y=40
    #player_two.location_x=1000
    #player_two.location_y=40
    P_one=Blue_player_hitbox(60,60)
    P_two=Red_player_hitbox(1000,60)
    
    player1_list.add(P_one)
    player2_list.add(P_two)
    i=0
    j=1
    # -------- Main Program Loop -----------
    while not done:
        #player hitbox locations+++++++++++++++++++++++++++++++++++++++++++++++++++
        predetor = graphic.R
        if i <= 60*20:
            predetor = graphic.R
        else:
            predetor = graphic.B
            if i == 60*40:
                i = 0
                j= -j

        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if  event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_a:
                    #player_one.movement_speed_x = -3
                    P_one.changespeed(-3,0)
                    player_one.direction=(0,0)
                if event.key == pygame.K_d:
                   # player_one.movement_speed_x = 3
                    P_one.changespeed(3,0)
                    player_one.direction=(1,1)
                if event.key == pygame.K_w:
                    #player_one.movement_speed_y = -3
                    P_one.changespeed(0,-3)
                    player_one.direction=(0,1)
                if event.key == pygame.K_s:
                    #player_one.movement_speed_y = 3
                    P_one.changespeed(0,3)
                    player_one.direction=(1,0)

            if  event.type == pygame.KEYUP:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_a:
                    #player_one.movement_speed_x = -3
                    P_one.changespeed(3,0)
                    player_one.direction=(0,0)
                if event.key == pygame.K_d:
                   # player_one.movement_speed_x = 3
                    P_one.changespeed(-3,0)
                    player_one.direction=(1,1)
                if event.key == pygame.K_w:
                    #player_one.movement_speed_y = -3
                    P_one.changespeed(0,3)
                    player_one.direction=(0,1)
                if event.key == pygame.K_s:
                    #player_one.movement_speed_y = 3
                    P_one.changespeed(0,-3)
                    player_one.direction=(1,0)
        #player two
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #player_two.movement_speed_x = -3
                    P_two.changespeed(-3,0)
                    player_two.direction=(0,0)
                if event.key == pygame.K_RIGHT:
                    #player_two.movement_speed_x = 3
                    P_two.changespeed(3,0)
                    player_two.direction=(1,1)
                if event.key == pygame.K_UP:
                    #player_two.movement_speed_y = -3
                    P_two.changespeed(0,-3)
                    player_two.direction=(0,1)
                if event.key == pygame.K_DOWN:
                    #player_two.movement_speed_y = 3
                    P_two.changespeed(0,3)
                    player_two.direction=(1,0)

            if  event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    #player_two.movement_speed_x = -3
                    P_two.changespeed(3,0)
                    player_two.direction=(0,0)
                if event.key == pygame.K_RIGHT:
                    #player_two.movement_speed_x = 3
                    P_two.changespeed(-3,0)
                    player_two.direction=(1,1)
                if event.key == pygame.K_UP:
                    #player_two.movement_speed_y = -3
                    P_two.changespeed(0,3)
                    player_two.direction=(0,1)
                if event.key == pygame.K_DOWN:
                    #player_two.movement_speed_y = 3
                    P_two.changespeed(0,-3)
                    player_two.direction=(1,0)

    #bullet++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if event.type == pygame.MOUSEBUTTONDOWN:
            if i >= 60*20 and j == 0:  
                j=1
                # Fire a bullet if the user clicks the mouse button
                bullet = Blue_Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = P_one.rect.x
                bullet.rect.y = P_one.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            elif i <= 60*20 and j == 1:
                j=0
                 # Fire a bullet if the user clicks the mouse button
                bullet = Red_Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = P_two.rect.x
                bullet.rect.y = P_two.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        # --- Game logic should go here
        

        P_one.move(current_room.wall_list)
        P_two.move(current_room.wall_list)
        if pygame.sprite.collide_rect(P_one,P_two):
            if predetor==graphic.R:
                player_data.player_one.life_Points-= player_data.player_two.atk_Power
                P_one.rect.x=60
                P_one.rect.y=60
                P_two.rect.x=1000
                P_two.rect.y=60
            else:
                player_data.player_two.life_Points-= player_data.player_one.atk_Power
                P_one.rect.x=60
                P_one.rect.y=60
                P_two.rect.x=1000
                P_two.rect.y=60

        #player_one.location_x += player_one.movement_speed_x
        #player_one.location_y += player_one.movement_speed_y
        #player_two.location_x += player_two.movement_speed_x
        #player_two.location_y += player_two.movement_speed_y

        #bullet++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #all_sprites_list.update()
        #for bullet in bullet_list:
 
        #    # See if it hit a block
        #    block_hit_list = pygame.sprite.spritecollide(bullet, player_one, True)
 
        #    # For each block hit, remove the bullet and add to the score
        #    for block in block_hit_list:
        #        bullet_list.remove(bullet)
        #        all_sprites_list.remove(bullet)
        #        player_one.life_Points-=2
        #        print(score)
 
        #    # Remove the bullet if it flies up off the screen
        #    if bullet.rect.y < -10:
        #        bullet_list.remove(bullet)
        #        all_sprites_list.remove(bullet)



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
        #map_selection = 2
        #running_map = map.map(map_selection)
        #map.map.draw_map(running_map)
        # --- Drawing character
        #player_one.color=graphic.B
        #player_two.color=graphic.R
        #draw character
        shape.predetor_sign(screen,predetor,550,50)
        #shape.draw_character_one(screen,player_one.location_x,player_one.location_y)
        #shape.draw_character_two(screen,player_two.location_x,player_two.location_y)
        player1_list.draw(screen)
        player2_list.draw(screen)
        current_room.wall_list.draw(screen)
        #all_sprites_list.draw(screen)
        #display update
        if player_data.player_two.life_Points<=0:
            screen.fill(W)
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over, P1 wins",True,BL)
            screen.blit(text,[540,350])
        elif player_data.player_one.life_Points<=0:
            screen.fill(W)
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over, P2 wins",True,BL)
            screen.blit(text,[540,350])
        pygame.display.flip()
    
        #FPS contral
        i += 1
        i
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()