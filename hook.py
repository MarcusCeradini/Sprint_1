import pygame
from viewport import viewport
from fish import fish
from state import state

class Hook:
    def __init__(self):
        self.x = 0
        self.y = 0
        
        self.radius = 5
        self.color = 'BLACK'

        self.max_speed = 10
        self.attached_fishes = []
        self.catch_distance = 20
        self.max_fish = 10
        self.pounds_caught = 0
    
    def cast(self):
        state['current_action'] = 'casting'
        self.x = viewport.width / 2
        self.y = viewport.width / 4

    # Used AI to help with the hook movement and collision detection
    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        cursor_y += viewport.y
        if state['current_action'] != 'reeling':
            self.x = cursor_x
            self.y = cursor_y
            # self.y = viewport.y + viewport.width / 2
            if state['current_action'] == 'waiting' and len(self.attached_fishes) != 0:
                fish_caught = self.attached_fishes.pop()
                self.pounds_caught += fish_caught.pounds
                fish_caught.caught = False # no longer in list of caught fish
            return
        
        dx = cursor_x - self.x
        dy = cursor_y - self.y
        magnitude = (dx * dx + dy * dy) ** .5
        if magnitude <= self.max_speed:
            self.x = cursor_x
            self.y = cursor_y
        else:
            # normalize then scale by speed
            self.x += dx / magnitude * self.max_speed
            self.y += dy / magnitude * self.max_speed
            
        
        # Check for fish collision if not at max capacity
        if len(self.attached_fishes) < self.max_fish:
            for fish_obj in fish:
                if fish_obj.caught:
                    continue
                if fish_obj.check_collision(self.x, self.y):
                    self.attached_fishes.append(fish_obj)
                    fish_obj.caught = True
                    break

    def draw(self, surface, current_round, cast):
        if state['current_action'] != 'waiting':
            pygame.draw.circle(surface, self.color, (self.x - viewport.x, self.y - viewport.y), self.radius) 
        
        # Draw fish counter in top right corner
        font = pygame.font.Font(None, 36)
        pounds_text = font.render(f"Pounds Caught: {self.pounds_caught}", True, (255, 255, 255))
        surface.blit(pounds_text, (20, 20)) 
        counter_text = font.render(f"Round: {current_round}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 20)) 
        counter_text = font.render(f"Cast: {cast}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 50)) 
        counter_text = font.render(f"Quota: {(current_round * 20)* 1.5}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 80))
        counter_text = font.render(f"Fish Caught: {len(self.attached_fishes)}", True, (255, 255, 255))
        surface.blit(counter_text, (surface.get_width() - counter_text.get_width() - 20, 110)) 
   
hook = Hook()