import pygame
import viewport

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.init()
        surface = pygame.display.set_mode((400, 300))
        color = (255, 0, 0)

        pygame.draw.rect(surface, color, pygame.Rect(30, 30, self.x, self.y))
        pygame.display.flip()
        pygame.time.wait(6000)
        pygame.quit()
    def update(self):
        pass
    def move(self):
        pass
    def reset(x, y):
        pass
    def update(self):
        pass

randomFish = Fish(40,30)
randomFish.draw()