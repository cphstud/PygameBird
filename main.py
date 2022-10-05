import sys
import pygame
import settings as s
from random import randint

gfactor=1
gf=5
direction=1
counter=0
gamedict={"counter":0, "level":1}
bird_speed=s.speed_bird
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #what should happen?
            print("MD")
            print(croshair_rect.center)
            print(bird_rect.center)

            if croshair_rect.colliderect(bird_rect):
                bird_rect.center=(s.width+10,randint(0,s.height))
                #counter=counter+1
                game_logic("hit")
        if event.type == pygame.MOUSEMOTION:
            pass
            #croshair_rect=croshair.get_rect(center = event.pos)

def game_logic(msg):
    if msg == "hit":
        gamedict["counter"]=gamedict["counter"]+1
    if gamedict["counter"]%gf==0:
        gamedict["level"]=gamedict["level"]+1


#define variables

pygame.init()
#set screen
screen=pygame.display.set_mode((s.width,s.height))
# init clock from time
clock=pygame.time.Clock()
myfont=pygame.font.SysFont("arial",32)
textbox=pygame.Rect(0,0,50,50)

# init load images
bg=pygame.image.load("resources/green2.jpg")
tree=pygame.image.load("resources/tree2.png")
bird=pygame.image.load("resources/bird.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.jpeg")
# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(s.width/2,s.height/2))
bird_rect=bird.get_rect(center=(s.xpos_bird,s.ypos_bird))
bird_dict={"link":bird,"rect":bird_rect,"speed":bird_speed}

#  create rect

#start the loop

while True:
    # check events with for-loop
    check_events()

    #put background on screen
    screen.blit(bg,(0,0))
    croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())
    #bird_rect.x = bird_rect.x - (s.speed_bird*gfactor*direction)
    bird_dict["rect"].x = bird_dict["rect"].x - (bird_dict["speed"]*gamedict["level"]*direction)

    #put paint stuff on screen
    screen.blit(tree,(s.xpos_tree,s.ypos_tree))
    screen.blit(bird,bird_rect)
    screen.blit(croshair,croshair_rect)
    text=myfont.render(f'score: {gamedict["counter"]}',s.black,s.green)
    screen.blit(text,textbox)

    #update screen
    pygame.display.update()
    clock.tick(s.framerate)
