import sys

import pygame

pygame.init()

screen=pygame.display.set_mode((400,600))
clock=pygame.time.Clock()

while True:
    # check events
    #$ev=pygame.event.get()
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()

    pygame.draw.line(screen,(220,223,123),(0,0),(100,100))
    clock.tick(30)
    pygame.display.flip()