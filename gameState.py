import random
from setup import WINDOW_WIDTH, WINDOW_HEIGHT
from fish import *

def start_cast(current_round):
    generate_fish(current_round)

PROBABILITIES = {
    Carp: .6,
    Salmon: .3,
    Swordfish: .1
}

CUMULATIVE_PROBABILITIES = PROBABILITIES.copy()
running_total = 0
for key in CUMULATIVE_PROBABILITIES:
    running_total += PROBABILITIES[key]
    CUMULATIVE_PROBABILITIES[key] = running_total

def generate_fish(current_round):
    fish_count = current_round * 10
    for i in range(fish_count):
        rng = random.random()
        for FishClass, probability in CUMULATIVE_PROBABILITIES.items():
            if rng < probability:
                fish.append(FishClass(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)))
