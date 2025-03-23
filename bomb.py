import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    """A class to manage bombs fired from the ship"""

    def __init__(self, ai_game):
        """Create a bomb object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bomb_color

        #Create a bomb rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midbottom = ai_game.ship.rect.midbottom

        #Store the bomb's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bomb down the screen."""
        #Update the decimal position of the bomb.
        self.y += self.settings.bomb_speed
        #Update the rect position
        self.rect.y = self.y

    def draw_bomb(self):
        """Draw the bomb to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)