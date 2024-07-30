import sys
import pygame # type: ignore
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and screen settings, and screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    ship = Ship(screen)
    running = True

    while running:
    # watch for events
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update_self()


run_game()
    