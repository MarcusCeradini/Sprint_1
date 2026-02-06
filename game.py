import pygame
import sys
pygame.init()

from viewport import viewport, create_viewport
 
# Colors
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
create_viewport(WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
 
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
    viewport.update()

    # update fish (plural)
    
    # draw hook
    # ..

    pygame.display.update()
    fpsClock.tick(FPS)
 
main()