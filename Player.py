import pygame 
import os 
from pygame.locals import *

class Player:
    def __init__(self, ypos):
        self.image = pygame.image.load('/Users/gregorirodriguez/Desktop/Games/Space_Invaders/InvadersImages/ship.png')
        self.x = 10
        self.y = ypos

    def update (self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 3
        elif keys[K_LEFT]:
            self.x -= 3

    def draw(self,screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])