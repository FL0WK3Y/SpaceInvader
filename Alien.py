import pygame

class Alien:
    def __init__(self, x,y, atype, imgfile):
        self.x =x
        self.y =y 
        self.atype = atype
        self.frame=0
        self.image = pygame.image.load("/Users/gregorirodriguez/Desktop/Games/Space_Invaders/InvadersImages/aliens_sm.png")
        self.sprite_size = 32
    
    def draw(self, screen):
        screen.blit(self.image, [self.x * self.sprite_size, self.y * self.sprite_size, self.sprite_size, self.sprite_size],(self.frame * self.sprite_size, self.sprite_size * self.atype, self.sprite_size,self.sprite_size))