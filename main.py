import sys
import pygame
import settings as s

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
                bird_rect.center=(s.width+100,s.height)
        if event.type == pygame.MOUSEMOTION:
            pass
            #croshair_rect=croshair.get_rect(center = event.pos)

#define variables

pygame.init()
#set screen
screen=pygame.display.set_mode((s.width,s.height))
# init clock from time
clock=pygame.time.Clock()

# init load images
bg=pygame.image.load("resources/green2.jpg")
tree=pygame.image.load("resources/tree2.png")
bird=pygame.image.load("resources/bird.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.jpeg")
# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(s.width/2,s.height/2))
bird_rect=bird.get_rect(center=(s.xpos_bird,s.ypos_bird))

#  create rect

#start the loop
active = False
counter = 0
while True:
    counter +=1
    # check events with for-loop
    check_events()

    #put background on screen
    screen.blit(bg,(0,0))
    croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())
    bird_rect.x = bird_rect.x - s.speed_bird

    #put paint stuff on screen
    screen.blit(tree,(s.xpos_tree,s.ypos_tree))
    screen.blit(bird,bird_rect)
    screen.blit(croshair,croshair_rect)

    #update screen
    pygame.display.update()
    clock.tick(s.framerate)
