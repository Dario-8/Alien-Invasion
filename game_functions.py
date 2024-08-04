import sys
import pygame
from ship import Ship
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown(event, ai_settings, screen, ship, bullets)
        check_keyup(event, ship)

def check_keydown(event, ai_settings, screen, ship, bullets):
    """check for Keydown events"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # RENDER YOUR GAME HERE
    ship.blitme()
    # flip() the display to put your work on screen
    pygame.display.flip()

