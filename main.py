import sys
import pygame
from random import randint

#define variables
width=600
height=400
delta=int(width/10)

xpos_bird=width-delta
ypos_bird=delta
xpos_tree=100
ypos_tree=100

speed_bird=1
framerate=120

pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# init clock from time
clock=pygame.time.Clock()

# init load images
bg=pygame.image.load("resources/green2.jpg")
tree=pygame.image.load("resources/tree2.png")

# load list of birds
birds=[]
for birdno in range(10):
    #tmpBird={"img":bird, "name":(f'Bird_{birdno}'), "counter":0, "xpos":randint((width-delta),width})}
    tmpxpos=randint((width-delta),width)
    tmpypos=randint((delta),4*delta)
    tmpspeed=randint(1,3)
    tmplink = pygame.image.load("resources/bird.png")
    tmpBird={"link":tmplink,"name":"Bird_"+str(birdno), "count":0,"xpos":tmpxpos,"ypos":tmpypos, "speed":tmpspeed}
    birds.append(tmpBird)

#start the loop
while True:
    # check events with for-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #put background on screen
    screen.blit(bg,(0,0))
    # modify moving objects
    for bird in birds:
        bird['xpos']-=bird['speed']
        screen.blit(bird['link'], (bird['xpos'],bird['ypos']))
    #put paint stuff on screen
    screen.blit(tree,(100,100))

    #update screen
    pygame.display.update()
    #tick the clock
    clock.tick(60)
