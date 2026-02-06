import pygame
import viewport

class Hook:
    def __init__(self):
        self.x
        self.y

    def update():
        cursor_x, cursor_y = pygame.mouse.get_pos()
        self.y = viewport.y + viewport.width/2
        self.x = cursor_x 

    def draw():
        pygame.Rect(self.x - viewport.x, self.y - viewport.y, 30, 30)
   

    