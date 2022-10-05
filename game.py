import sys

from ship import Ship
from bullet import Bullet
import pygame
import settings as s

pygame.init()
screen=pygame.display.set_mode((s.width,s.height))
clock=pygame.time.Clock()
shipimg=pygame.image.load("resources/spac.jpeg")
shipimg=pygame.transform.scale(shipimg,(55,55))
myship=Ship(s.width/2,s.height,shipimg,screen)
myship.loadbullets(10)
#test
testbullet=Bullet(s.width/2,s.height-50,2,10,(23,45,32),screen)
testbullet.fire()


while True:
    screen.fill(s.bgcol)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(f"in {event.type}")
            if event.key == pygame.K_RIGHT:
                myship.moveright=True
                print(f"got {myship.moveright}")
            elif event.key == pygame.K_LEFT:
                myship.moveleft=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                myship.moveright=False
            elif event.key == pygame.K_LEFT:
                myship.moveleft=False
            elif event.key == pygame.K_SPACE:
                print("SPACE")
                myship.firebullets(screen)

    # set dynamic variables
    myship.move()
    #$myship.automove()
    #testbullet.fire()
    myship.render(screen)
    #
    pygame.display.update()
    clock.tick(4)



