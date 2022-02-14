import pygame
from random import randint

class Bird():
    #the attributes are initialized  in the  constructor

    #the constructor

    def __init__(self,screen,namefeed,link):
        w, h = pygame.display.get_surface().get_size()
        delta=w/10
        self.screen=screen
        self.namefeed=namefeed
        self.xpos=randint((w-delta),w)
        self.ypos=randint((delta),4*delta)
        self.speed=randint(1,3)
        self.link=pygame.image.load(link)

    #the methods

    def set_xpos(self):
        pass

    def set_ypos(self):
        pass

    def set_speed(self,speed):
        self.speed=speed

    def move(self):
        self.xpos -=self.speed

    def blitme(self):
        self.screen.blit(self.link,(self.xpos,self.ypos))