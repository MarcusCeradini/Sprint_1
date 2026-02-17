import pygame
import sys
pygame.init()

from setup import *
import gameState
from viewport import viewport
from fish import fish
from hook import hook
from state import state
# Colors
BACKGROUND = (0, 100, 255)

# Game Setup
fpsClock = pygame.time.Clock()

viewport.width = WINDOW_WIDTH
viewport.height = WINDOW_HEIGHT
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fshng Game')

current_round = 0
max_round = 5

def main():
    global current_round
    looping = True

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if state['current_action'] == 'waiting':
                    hook.cast()
                    gameState.start_cast(current_round)
                    current_round += 1

        # Render elements of the game
        screen.fill(BACKGROUND)
        if viewport.y < 0:
            pygame.draw.rect(screen, (0, 200, 255), pygame.Rect(0, 0, WINDOW_WIDTH, -viewport.y))


        # Game logic

        # update hook
        hook.update()

        # update viewport
        viewport.update()

        # update fish (plural)

        for element in fish:
            element.update(hook)

        # draw fish
        for element in fish:
            element.draw(screen)

        # draw hook
        hook.draw(screen, current_round)
        
        # Used AI to fix fish not being gotten rid of when caught issue
        pygame.display.update()
        fpsClock.tick(FPS)

main()
