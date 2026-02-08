import pygame
from viewport import viewport

class Hook:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 'BLACK'

    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        # print(cursor_x, cursor_y)
        self.y = viewport.y + viewport.width/2
        self.x = cursor_x 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x - viewport.x, self.y - viewport.y), 5) 
   
hook = Hook()