import sys
import pygame

# initialize variables
direction=1
width=600
height=400
delta=50
speed=3
xpos=width-delta

# first step
pygame.init()

# define base surface
screen = pygame.display.set_mode((width,height))

# load objects to be displayed on surface
bgpicture=pygame.image.load("resources/green2.png")
tree=pygame.image.load("resources/tree2.png")
bird=pygame.image.load("resources/bird.png")
clock=pygame.time.Clock()

# start game loop

while True:
    # tjek events
    #for event in pygame.event.get():
    #    if event.type == pygame.Q
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()


    xpos=xpos-(speed*direction)
    if xpos < 0 or xpos > width:
        direction=direction*-1
        bird=pygame.transform.flip(bird,True,False)

    screen.blit(bgpicture, (0,0))
    screen.blit(bird,(xpos,200))
    screen.blit(tree,(200,100))

    clock.tick(30)
    pygame.display.flip()

