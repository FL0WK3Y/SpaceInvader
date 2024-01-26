import pygame 
from Bullet import Bullet
from pygame.locals import *
import Settings

class Player(pygame.sprite.Sprite):
    def __init__(self, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/Users/gregorirodriguez/Desktop/Games/Space_Invaders/InvadersImages/ship.png')
        self.x = 10
        self.y = ypos
        self.bullets = []
        self.font = pygame.font.SysFont('Arial',25)
        self.lives = 3
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

    def update (self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 3
            
        elif keys[K_LEFT]:
            self.x -= 3
        self.rect.topleft = (self.x,self.y)
        if keys[K_SPACE]:
            self.bullets.append(Bullet(self.x + self.image.get_width()//2 ,self.y,23))
        for l in pygame.sprite.spritecollide(self,Settings.abullets,0):
            Settings.abullets.remove(l)
            l.kill()
            self.lives -= 1 



    def draw(self,screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])
        self.lives_text = self.font.render('lives: ' + str(self.lives), True, (255,100,100))
        screen.blit(self.lives_text,(0,0))
        
        deadbullets = []
        for b in self.bullets:
            if b.y < 0 :
                deadbullets.append(b)
            b.draw(screen)
        for b in deadbullets:
            self.bullets.remove(b)
