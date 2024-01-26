import pygame
import random
from Player import Player
from Alien import Alien
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
    def update(self, events):        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousex, self.mousey = event.pos
                if self.button_rect[0] <= self.mousex <= self.button_rect[0] + self.button_rect[2] and self.button_rect[1] <= self.mousey <= self.button_rect[1] + self.button_rect[3]:   
                    return self.main_menu
            if event.type == pygame.MOUSEMOTION:
                self.mousex, self.mousey = event.pos
        self.player.update()
        return self
    
    def draw(self, screen):
        if self.button_rect[0] <= self.mousex <= self.button_rect[0] + self.button_rect[2] and self.button_rect[1] <= self.mousey <= self.button_rect[1] + self.button_rect[3]:  
            pygame.draw.rect(screen,self.button_over_color, self.button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, (self.button_rect[0]+ (self.button_width - self.button_text.get_width()) /2, self.button_rect[1]+ (self.button_height - self.button_text.get_height()) /2 ))
        

        for a in self.aliens:
            a.draw(screen)
        
        self.player.draw(screen)
        
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