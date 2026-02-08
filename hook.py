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
        self.fish_caught = 0

    # Used AI to help with the hook movement and collision detection
    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        # print(cursor_x, cursor_y)
        self.y = viewport.y + viewport.width/2
        self.x = cursor_x 
        
        # Check for fish collision if not at max capacity
        if len(self.attached_fishes) < self.max_fish:
            for fish_obj in fish:
                distance = ((self.x - fish_obj.x)**2 + (self.y - fish_obj.y)**2)**0.5
                if distance < self.catch_distance:
                    self.attached_fishes.append(fish_obj)
                    fish.remove(fish_obj)
                    self.fish_caught += 1
                    break
        
        # Update attached fish positions to follow hook
        for attached_fish in self.attached_fishes:
            attached_fish.x = self.x
            attached_fish.y = self.y + 10 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x - viewport.x, self.y - viewport.y), 5) 
        
        # Draw attached fish if there are any
        if self.attached_fishes:
            for attached_fish in self.attached_fishes:
                attached_fish.draw(surface) 
        
        # Draw fish counter in top right corner
        font = pygame.font.Font(None, 36)
        counter_text = font.render(f"Fish Caught: {self.fish_caught}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 20)) 
   
hook = Hook()