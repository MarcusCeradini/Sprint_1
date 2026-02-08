import pygame
from viewport import viewport

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self, surface):
        color = (255, 0, 0)
        pygame.draw.rect(surface, color, pygame.Rect(self.x - viewport.x, self.y - viewport.y, 10, 10))

    def reset(x, y):
        pass

fish = []