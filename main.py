import sys
import pygame
import settings as s
from random import randint

#define variables
white=(250,250,250)
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
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.jpeg")
# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(width/2,height/2))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))

# multiple birds
delta=s.height-s.height/10
listofbirds=[]
for i in range(0,s.numofbirds):
    link=pygame.image.load("resources/bird.png")
    speed=randint(1,4)
    ypos=randint(s.height-delta,s.height)
    xpos=randint(s.width,s.width+delta)
    bird_rect=link.get_rect(center=(xpos,ypos))
    tmpbird = {"name":f"bird_{i}",
               "link":link,
               "rect":bird_rect,
               "counter":0,
               "xpos":xpos,
               "ypos":ypos,
               "speed":speed,
               "direction":1
               }
    listofbirds.append(tmpbird)

#  create rect

#start the loop
active = False
counter = 0
while True:
    counter +=1
    # check events with for-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #what should happen?
            if croshair_rect.colliderect(bird_rect):
                xpos_bird=width+100
        if event.type == pygame.MOUSEMOTION:
            pass
            #croshair_rect=croshair.get_rect(center = event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                active=not active
    #put background on screen
    screen.blit(bg,(0,0))
    # modify moving objects
    croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())

    for bird in listofbirds:
        bird["xpos"]=bird["xpos"]-(bird["speed"]*bird["direction"])
        bird["rect"].x = bird["xpos"]

    #put paint stuff on screen

    for bird in listofbirds:
        screen.blit(bird["link"],bird["rect"])
    screen.blit(croshair,croshair_rect)

    screen.blit(tree,(100,100))

    #update screen
    pygame.display.update()
    clock.tick(30)
#tick the clock
