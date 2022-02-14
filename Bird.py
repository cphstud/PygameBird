import pygame

class Bird():
    #the attributes are initialized  in the  constructor
    # name,xpos,ypos,speed,link
    #the constructor
    def __init__(self,screen,name,xpos,ypos,speed,link):
        self.screen=screen
        self.name=name
        self.xpos=xpos
        self.ypos=ypos
        self.speed=speed
        self.link=link

    #the methods

    def set_speed(self,speed):
        self.speed=speed

    def move(self):
        self.xpos +=self.speed

    def blitme(self):
        self.screen.blit(self.link)