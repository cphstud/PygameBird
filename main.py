import sys
import pygame

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
bird=pygame.image.load("resources/bird.png")

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
    xpos_bird=xpos_bird-speed_bird

    #put paint stuff on screen
    screen.blit(tree,(100,100))
    screen.blit(bird,(xpos_bird,ypos_bird))

    #update screen
    pygame.display.update()
    #tick the clock
    clock.tick(120)
