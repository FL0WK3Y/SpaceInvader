import pygame

class Bullet:
    def __init__(self,x,y,yspeed):
        self.image = pygame.image.load('/Users/gregorirodriguez/Desktop/Games/Space_Invaders/InvadersImages/bullet.png')
        self.x = x - self.image.get_width()//2
        self.y = y
        self.dy = yspeed
        
    def draw(self,screen):
        self.y -= self.dy
        screen.blit(self.image,[self.x, self.y, self.image.get_width(),self.image.get_height()])