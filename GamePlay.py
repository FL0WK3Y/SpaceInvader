import pygame
import random
from Player import Player
from Alien import Alien
from Explosion import Explosion
import Settings

class GamePlay:
    def __init__(self, screen) :
        self.font = pygame.font.SysFont('Arial',30, True, False)
        self.title = self.font.render("This is where the game is ",True,(255,255,255))
        self.title_position = (10,10)
        self.main_menu = None
        self.text_color = (255,255,255)
        self.button_color =(0,0,170)
        self.button_over_color = (255,50,50)
        self.button_width = 50
        self.button_height = 20
        self.button_rect = [screen.get_width() - self.button_width,0 ,self.button_width, self.button_height]
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.button_text = self.button_font.render("Back", True, self.text_color)
        self.mousex , self.mousey =(0,0) 
        self.player = Player(screen.get_height() - 100)
        self.aliens = []
        self.alienrows = 5
        self.aliencols = 15
        for y in range (self.alienrows):
            for x in range(self.aliencols):
                self.aliens.append(Alien(x,y,random.randint(0,1)))
        self.left_border = 50
        self.right_border = screen.get_width() - self.left_border
        self.dx = 2
        self.dy = 10
        self.direction = self.dx
        self.explosions = []
        self.font2 = pygame.font.SysFont('Arial',80, True, False)
        self.title = self.font2.render("Game over ",True,(255,255,255))
        self.title_position = ((screen.get_width()- self.title.get_width())//2,(screen.get_height() - self.title.get_height())//2)

        self.title_won = self.font2.render("You Won",True,(255,255,255))
        self.title_position_won = ((screen.get_width()- self.title_won.get_width())//2,(screen.get_height() - self.title_won.get_height())//2)
        self.screen = screen
    
    def update(self, events):        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousex, self.mousey = event.pos
                if self.button_rect[0] <= self.mousex <= self.button_rect[0] + self.button_rect[2] and self.button_rect[1] <= self.mousey <= self.button_rect[1] + self.button_rect[3]:   
                    
                    #reset values when click back button 
                    self.player = Player(self.screen.get_height() - 100)
                    self.aliens = []
                    self.alienrows = 5
                    self.aliencols = 15
                    self.lives = 3
                    Settings.xoffset = 10
                    Settings.yoffset = 50
                    Settings.abullets = []
                    for y in range (self.alienrows):
                        for x in range(self.aliencols):
                            self.aliens.append(Alien(x,y,random.randint(0,1)))

                    
                    
                    return self.main_menu
            if event.type == pygame.MOUSEMOTION:
                self.mousex, self.mousey = event.pos
        self.player.update()

        found =False
        deadbullets = []
        if self.player.bullets != [] and self.aliens != []:
            for b in self.player.bullets:
                found = False
                #this spritecollide is determining whether a bullet is colliding with an alien 
                for a in pygame.sprite.spritecollide(b,self.aliens, 0 ):
                    self.aliens.remove(a)
                    self.explosions.append(Explosion(a.x,a.y))
                    a.kill()
                    found = True
                if found:
                    deadbullets.append(b)
            for b in deadbullets:
                self.player.bullets.remove(b)
                b.kill()

        return self
    
    def draw(self, screen):
        if self.button_rect[0] <= self.mousex <= self.button_rect[0] + self.button_rect[2] and self.button_rect[1] <= self.mousey <= self.button_rect[1] + self.button_rect[3]:  
            pygame.draw.rect(screen,self.button_over_color, self.button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, (self.button_rect[0]+ (self.button_width - self.button_text.get_width()) /2, self.button_rect[1]+ (self.button_height - self.button_text.get_height()) /2 ))
        if self.player.lives<=0:
            screen.blit(self.title,self.title_position)
            return self
        elif len(self.aliens)<= 0:
            screen.blit(self.title_won,self.title_position_won)
            return self

        for a in self.aliens:
            a.draw(screen)
        
        self.player.draw(screen)
        
        deadabullets = []
        
        for l in Settings.abullets:
            if l.y > screen.get_height():
                deadabullets.append(l)
            l.draw(screen)
        for l in deadabullets:
            Settings.abullets.remove(l)
        
        update_y = False
        if(Settings.xoffset+self.aliencols * 32) > self.right_border:
            self.direction *= - 1
            update_y = True
            Settings.xoffset = self.right_border - self.aliencols * 32 
        
        if Settings.xoffset < self.left_border:
            self.direction *= - 1
            update_y = True
            Settings.xoffset =self.left_border
        Settings.xoffset += self.direction
        
        if update_y :
            Settings.yoffset += self.dy

        deadexplosions=[]
        for e in self.explosions:
            e.draw(screen)
            if e.framey < 0:
                deadexplosions.append(e)
        for e in deadexplosions:
            self.explosions.remove(e)

