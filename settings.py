# a class to store all the settings for alien invasion

class Settings():
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = "ALIEN INVASION"

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_color = (0, 0, 0)
        self.bullet_width = 3
        self.bullet_height = 20
        self.speed_factor = 1