class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (10, 10, 10)
        
        #Ship settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 3

        #Bomb settings
        self.bomb_width = 20
        self.bomb_height = 60
        self.bomb_color = (200, 200, 200)
        self.bombs_allowed = 1
        self.shrapnel_color = (200, 200, 200)
        self.shrapnel_width = 15
        self.shrapnel_height = 3

        #Alien settings
        self.fleet_drop_speed = 10
        
        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bomb_speed = 0.3
        self.alien_speed = 0.5

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

        
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        