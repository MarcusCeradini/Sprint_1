import pygame
import viewport

class Fish:
    def __init__(self):
        self.x
        self.y
    
    def update(self):
        pass

    def draw(self):
        pygame.Rect(self.x - viewport.x, self.y - viewport.y, 30, 30)

fish = [
    Fish(),
    Fish(),
    Fish(),
    Fish()
]