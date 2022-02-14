import sys
import pygame
from Bird import Bird

#define variables
width=600
height=400
xpos_tree=100
ypos_tree=100
framerate=120

pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# init clock from time
clock=pygame.time.Clock()

# init load images
bg=pygame.image.load("resources/green2.jpg")
tree=pygame.image.load("resources/tree2.png")
aim=pygame.image.load("resources/crosshair.png")

# load list of birds
birds=[]
for birdno in range(10):
    tmpBird=Bird(screen,birdno,"resources/bird.png")
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
        bird.move()
        bird.blitme()
    #put paint stuff on screen
    screen.blit(tree,(100,100))
    screen.blit(aim,((pygame.mouse.get_pos())))

    #update screen
    pygame.display.update()
    #tick the clock
    clock.tick(60)
