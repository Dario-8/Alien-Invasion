import sys
import pygame
from ship import Ship


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(ai_settings.bg_color)

    # RENDER YOUR GAME HERE
    ship.blitme()

    
    # flip() the display to put your work on screen
    pygame.display.flip()