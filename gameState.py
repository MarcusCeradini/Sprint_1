import random
from fish import fish, Fish

def start_cast(current_round):
    generate_fish(current_round)

def generate_fish(current_round):
    fish_count = current_round * 10
    for i in range (fish_count):
        fish.append(Fish())
