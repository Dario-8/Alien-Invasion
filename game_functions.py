import sys
import pygame
from ship import Ship


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False



def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(ai_settings.bg_color)

    # RENDER YOUR GAME HERE
    ship.blitme()

    
    # flip() the display to put your work on screen
    pygame.display.flip()