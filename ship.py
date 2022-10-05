import pygame
import settings as s
from bullet import Bullet

class Ship:
    # xpos
    # ypos
    # direction
    # moving
    # listofbullets

    def __init__(self,xpos,ypos,link,screen):
        self.screen=screen
        self.xpos=xpos
        self.ypos=ypos
        self.img=link
        self.rect=self.img.get_rect(center=(xpos,(ypos-20)))
        self.moveleft=False
        self.moveright=False
        self.movespeed=10
        self.direction=1
        self.listofbullets=[]
        self.isfired=False

    def render(self, screen):
        screen.blit(self.img, self.rect)
        # also render ship-bullets
        for bullet in self.listofbullets:
            if bullet.isfired:
                bullet.move()
                bullet.render()

    def move(self):
        # moving-logic bound to the x-axis
        print(f"into move {self.moveleft} and {self.moveleft}")
        if(self.moveright):
            self.xpos=self.xpos+self.movespeed
        elif(self.moveleft):
            self.xpos=self.xpos-self.movespeed
        self.rect.x=self.xpos

    def automove(self):
        print("into self move")
        if (self.xpos > 0 or self.xpos < s.width):
            print("xpos move")
            self.xpos=self.xpos+(self.xpos*self.movespeed*self.direction)
        else:
            self.direction=self.direction*-1
        self.rect.x=self.xpos

    def firebullets(self,screen):
        for bullet in self.listofbullets:
            bullet.fire()

    def loadbullets(self, numofbullets=10,bspeed=5,size=5,bcol=(45,45,145)):
        delta = size+2
        for i in range(0,3):
            tmpbullet=Bullet(self.xpos,self.ypos + (delta),bspeed,size,bcol,self.screen)
            tmpbullet.to_string()
            self.listofbullets.append(tmpbullet)
            delta=delta+size+2


