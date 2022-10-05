import sys
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

#  create rect

#start the loop
active = False
counter = 0
while True:
    # check events with for-loop
    counter +=1
    print(f"running {counter}")
    croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())
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
    if not active:
        screen.fill(white)
        screen.blit(startbut,(150,100))
    # modify moving objects
    else :
        xpos_bird=xpos_bird-speed_bird
        bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
        #put paint stuff on screen
        screen.blit(tree,(100,100))
        screen.blit(bird,bird_rect)
        screen.blit(croshair,croshair_rect)

    #update screen
    pygame.display.update()
#tick the clock
clock.tick(60)
