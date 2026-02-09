from setup import WINDOW_WIDTH, WINDOW_HEIGHT, cast_distance

from state import state

class Viewport:
    SPEED_CASTING = 20
    SPEED_REELING = -3
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
    def update(self):
        if state['current_action'] == 'waiting':
            self.x = 0
        elif state['current_action'] == 'casting':
            self.y += Viewport.SPEED_CASTING
            if self.y + self.height >= cast_distance:
                state['current_action'] = 'reeling'
        elif state['current_action'] == 'reeling':
            self.y += Viewport.SPEED_REELING
            if self.y <= -self.height * 2 / 3:
                state['current_action'] = 'waiting'


# Viewport follows hook
# An offset of half so then hook is centered
# View port - half hook position 

viewport = Viewport()