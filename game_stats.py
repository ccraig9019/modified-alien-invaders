import os
import sys

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start Alien Invasion in an inactive state
        self.game_active = False

        #High score should never be reset
        if getattr(sys, 'frozen', False):
            high_score_path = os.path.join(sys._MEIPASS, 'high_score.txt')
        else:
            high_score_path = 'high_score.txt'
        with open(high_score_path) as f:
            lines = f.readline() 
        self.high_score = int(lines)

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
