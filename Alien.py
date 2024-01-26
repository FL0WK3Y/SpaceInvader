import pygame
import Settings

class Alien:
    def __init__(self, x,y, atype,):
        self.x =x
        self.y =y 
        self.atype = atype
        self.frame = 0
        self.image = pygame.image.load("/Users/gregorirodriguez/Desktop/Games/Space_Invaders/InvadersImages/aliens_sm.png")
        self.sprite_size = 32
        

    def flip_frame(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0
    def draw(self, screen):
        if Settings.xoffset % 10 == 0:
            self.flip_frame()

        screen.blit(self.image, [self.x * self.sprite_size + Settings.xoffset, self.y * self.sprite_size + Settings.yoffset, self.sprite_size, self.sprite_size],(self.frame * self.sprite_size, self.sprite_size * self.atype, self.sprite_size,self.sprite_size))