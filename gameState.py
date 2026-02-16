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
    if (current_round == 3):
        """" TODO: Add an end screen, as well as adding the shark ending
             toggles screen for 5 seconds and instructs the user to run the game again to """
        print("You reached the ending of the game")
        pygame.quit()
