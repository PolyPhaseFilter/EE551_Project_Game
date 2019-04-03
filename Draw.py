import math
import pygame
import graphic

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
for i in range(200):

    radians_x = i / 20
    radians_y = i / 6

    x = int(75 * math.sin(radians_x)) + 200
    y = int(75 * math.cos(radians_y)) + 200

pygame.draw.line(set_screen, BL, [x, y], [x+5, y], 5)


