import pygame


class Bullet:
    # xpos
    # ypos
    # speed
    # size

    def __init__(self, xpos,ypos,speed,size,color,screen):
        self.screen=screen
        self.xpos=xpos
        self.ypos=xpos
        self.speed=speed
        self.size=size
        self.img=pygame.image.load("resources/ball.jpeg")
        self.color=(23,23,123)
        self.rect=pygame.Rect(xpos,ypos,size,size)
        self.isfired=False

    def render(self):
        print("print bullet")
        pygame.draw.rect(self.screen,self.color,self.rect)

    def move(self):
        self.rect.y = self.rect.y - self.speed

    def fire(self):
        print("Bullet will fire")
        self.rect.y = self.rect.y - self.speed
        self.render()
        self.isfired=True

    def to_string(self):
        print(f"x: {self.xpos}, y: {self.ypos}, c: {self.color}, s: {self.size}")



