from setup import WINDOW_WIDTH, WINDOW_HEIGHT

class Viewport:
    def __init__(self, window_width, window_height):
        self.x = 0
        self.y = 0
        self.vy = -1
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
    def update(self):
        self.y += self.vy

# Viewport follows hook
# An offset of half so then hook is centered
# View port - half hook position 

viewport = Viewport(0, 0)