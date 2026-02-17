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

current_round = 1
cast = 0
max_round = 5

def main():
    global current_round
    global cast

    # The main game loop
    while True:
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if state['current_action'] == 'waiting':
                    hook.cast()
                    cast += 1
                    current_round = int((cast - 1) / 3) + 1
                    if hook.pounds_caught == (current_round * 20):
                        print("You caught enough fish to feed the shark")
                    elif current_round == max_round:
                        print("Congrats you won")
                        pygame.quit()
                    elif cast == 3 and hook.pounds_caught != (current_round * 20):
                        print("Sorry you lose")
                        pygame.quit()
                    gameState.start_cast(current_round, cast)

        # Render elements of the game
        screen.fill(BACKGROUND)
        if viewport.y < 0:
            pygame.draw.rect(screen, (0, 200, 255), pygame.Rect(0, 0, WINDOW_WIDTH, -viewport.y))


        # Game logic

        # update hook
        hook.update()

        # update viewport
        viewport.update()
        
        # check if game is over
        if current_round == 2 and state['current_action'] == 'waiting':
            state['game_ended'] = True
            print("You reached the ending of the game")
            gameState.draw_end_screen()

        # update fish (plural)

        for element in fish:
            element.update(hook)

        # draw fish
        for element in fish:
            element.draw(screen)

        # draw hook
        hook.draw(screen, current_round, cast)
        
        # Used AI to fix fish not being gotten rid of when caught issue
        pygame.display.update()
        fpsClock.tick(FPS)

        if state['game_ended']:
            break
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
