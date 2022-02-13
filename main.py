import sys
import pygame

pygame.init()
#set screen
screen=pygame.display.set_mode((600,400))
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
    #put paint stuff on screen
    screen.blit(tree,(100,100))
    screen.blit(bird,(50,50))

    #update screen
    pygame.display.update()
    #tick the clock
    clock.tick(120)
