import random
from setup import WINDOW_WIDTH, WINDOW_HEIGHT, cast_distance
import pygame
from fish import *

def start_cast(current_round):
    print('New round!')
    generate_fish(current_round)

PROBABILITIES = {
    Carp: .5,
    Goldfish: .25,
    Salmon: .15,
    Swordfish: .1
}

CUMULATIVE_PROBABILITIES = PROBABILITIES.copy()
running_total = 0
for key in CUMULATIVE_PROBABILITIES:
    running_total += PROBABILITIES[key]
    CUMULATIVE_PROBABILITIES[key] = running_total

def generate_fish(current_round):
    fish_count = 10 + current_round * 2
    fish.clear()
    for i in range(fish_count):
        rng = random.random()
        for FishClass, probability in CUMULATIVE_PROBABILITIES.items():
            if rng < probability:
                fish.append(FishClass(random.randint(0, WINDOW_WIDTH), random.randint(0, cast_distance)))
                break

image = pygame.image.load("Sprites/LeftSharkFIRE.png")

def draw_end_screen(screen):
        WIDTH, HEIGHT = 960, 600

        # Set a opaque overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Draw image to the center
        image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(image, image_rect)
        
        #font = pygame.font.Font(None, 36)
        #pounds_text = font.render("Game End!", True, (255, 255, 255))
        #screen.blit(pounds_text, (20, 20))
        


