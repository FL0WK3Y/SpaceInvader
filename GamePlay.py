import pygame
from Player import Player
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
        self.player.draw(screen)