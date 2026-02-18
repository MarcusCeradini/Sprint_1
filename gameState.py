import random
from setup import WINDOW_WIDTH, WINDOW_HEIGHT, cast_distance
import pygame
from fish import *
from hook import *

def start_cast(current_round):
    print('New cast!')
    generate_fish(current_round)

PROBABILITIES = {
    Carp: .5,
    Goldfish: .25,
    Salmon: .15,
    Swordfish: .15
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


def draw_end_screen(screen, won):
    image = pygame.image.load("Sprites/LeftSharkFIRE.png")
    WIDTH, HEIGHT = 960, 600

    # Set a opaque overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    # # Draw image to the center
    # screen.blit(image, (0, 0))
    # print(image_rect)
    image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(image, image_rect)
        
    font = pygame.font.Font(None, 70)
    text = font.render("You won!" if won else "You lost", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.width / 2, screen.height / 6))
    screen.blit(text, text_rect)
    
    pygame.display.update()