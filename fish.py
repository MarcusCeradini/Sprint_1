import pygame
from viewport import viewport

# abstract class
class Fish:
    def __init__(self, x, y, xv = 0, yv = 0):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.caught = False

        self.color = (255, 0, 0)

    def update(self, hook):
        if self.caught:
            # Update attached fish positions to follow hook
            self.x = hook.x
            self.y = hook.y + 10 
    
    def check_collision(self, x, y):
        # rectangle to point collision detection
        return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x - viewport.x, self.y - viewport.y, self.width, self.height))

    def reset(x, y):
        pass

# Carp, Salmon , Swordfish
# PufferFish

class Carp(Fish):
    def __init__(self, x, y, xv = 0, yv = 0):
        super().__init__(x, y, xv, yv)
        self.width = 50
        self.height = 30

        self.color = (200, 0, 0)
        
class Salmon(Fish):
    def __init__(self, x, y, xv = 0, yv = 0):
        super().__init__(x, y, xv, yv)
        self.width = 50
        self.height = 30

        self.color = (255, 0, 0)

class Swordfish(Fish):
    def __init__(self, x, y, xv = 0, yv = 0):
        super().__init__(x, y, xv, yv)
        self.width = 125
        self.height = 80

        self.color = (0, 0, 220)

fish = []