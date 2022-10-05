import sys
from random import randint
import pygame

#define variables
white=(250,250,250)
width=600
height=400
delta=int(width/10)

xpos_bird=width-delta
ypos_bird=delta
xpos_tree=100
ypos_tree=100

speed_bird=3
framerate=120

pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# font for text
myfont = pygame.font.SysFont("arial",30)
# init clock from time
clock=pygame.time.Clock()

# init load images
bg=pygame.image.load("resources/green2.jpg")
tree=pygame.image.load("resources/tree2.png")
bird=pygame.image.load("resources/bird.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.jpeg")
# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(width/2,height/2))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))

#  create rect
active = False
counter = 1
level = 1
gamedict={"counter":1,"level":0, "liv":3}
#start the loop
while True:
    # har jeg liv til at fortsætte?
    if gamedict["liv"]==0:
        active = False
        screen.fill(white)
        screen.blit(startbut,(150,100))
        pygame.quit()
        sys.exit()
    else:
        # check events with for-loop
        croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #what should happen?
                if croshair_rect.colliderect(bird_rect):
                    #counter = counter + 1
                    gamedict["counter"]=gamedict["counter"]+1
                    xpos_bird=width
                    # random ypos for bird
                    ypos_bird=randint(0,height)
            if event.type == pygame.MOUSEMOTION:
                pass
                #croshair_rect=croshair.get_rect(center = event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    active=not active
        #put background on screen
        screen.blit(bg,(0,0))
        if not active:
            screen.fill(white)
            screen.blit(startbut,(150,100))
        # modify moving objects
        else :
            # adjust speed according to counter/score
            if gamedict["counter"] % 5 == 0:
                print("in counter")
                gamedict["counter"]=1
                gamedict["level"] = gamedict["level"] + 1
                speed_bird=speed_bird+1
            # hvis xpos < 0 så miste et liv
            if (xpos_bird < 0):
                gamedict["liv"]=gamedict["liv"]-1
                xpos_bird=width
                ypos_bird=randint(0,height)
            else:
                xpos_bird=xpos_bird-speed_bird
            bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
            #put paint stuff on screen
            # put counter on screen
            textobj=myfont.render(f'Score: {gamedict["counter"]}, level: {gamedict["level"]},liv: {gamedict["liv"]}',(0,0,0),(255,255,255))
            screen.blit(textobj,(0,0))
            screen.blit(tree,(100,100))
            screen.blit(bird,bird_rect)
            screen.blit(croshair,croshair_rect)

        #update screen
        pygame.display.update()
    #tick the clock
        clock.tick(60)
