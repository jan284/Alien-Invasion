class Settings:
    """Class to store all the setting for Alien Invasion"""

    def __init__(self):
        """Initialize game's settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_colour = (32, 178, 170)
        self.ship_speed = 5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (68, 17, 74)


