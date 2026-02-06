import pygame
import sys
pygame.init()


import gameState
from viewport import viewport
from fish import fish
 
# Colors
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

current_round = 1
 
def main():
  looping = True
  
  # The main game loop
  while looping:
    # Get inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    # Game logic

    # update hook
    
    # update viewport

    # update fish (plural)
    
    for element in fish:
      element.update()
      
    # draw hook
    for element in fish:
      element.draw()

    pygame.display.update()
    fpsClock.tick(FPS)
 
main()