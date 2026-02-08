import pygame
from viewport import viewport
from fish import fish

class Hook:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 'BLACK'
        self.attached_fishes = []
        self.catch_distance = 20
        self.max_fish = 5

    # Used AI to help with the hook movement and collision detection
    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        # print(cursor_x, cursor_y)
        self.y = viewport.y + viewport.width/2
        self.x = cursor_x 
        
        # Check for fish collision if not at max capacity
        if len(self.attached_fishes) < self.max_fish:
            for fish_obj in fish:
                if fish_obj.caught:
                    break
                if fish_obj.check_collision(self.x, self.y):
                    self.attached_fishes.append(fish_obj)
                    print('caught!')
        
        # Update attached fish positions to follow hook
        for attached_fish in self.attached_fishes:
            attached_fish.x = self.x
            attached_fish.y = self.y + 10 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x - viewport.x, self.y - viewport.y), 5) 
        
        # Draw fish counter in top right corner
        font = pygame.font.Font(None, 36)
        counter_text = font.render(f"Fish Caught: {len(self.attached_fishes)}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 20)) 
   
hook = Hook()