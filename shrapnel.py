import pygame
from pygame.sprite import Sprite

class Shrapnel(Sprite):
    """A class to manage shrapnel released from a bomb"""

    def __init__(self, ai_game, bomb):
        """Create a shrapnel object at the bomb's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.shrapnel_color

        #Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.shrapnel_width, self.settings.shrapnel_height)
        
        self.rect.center = bomb.rect.center

        #Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the shrapnel across the screen."""
        #Update the decimal position of the shrapnel.
        self.x += self.settings.shrapnel_speed
        #Update the rect position
        self.rect.x = self.x

    def draw_shrapnel(self):
        """Draw the shrapnel to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)