import pygame
from pygame.sprite import Sprite

class Shrapnel(Sprite):
    """A class to manage shrapnel released from a bomb"""

    def __init__(self, ai_game, bomb, direction):
        """Create a shrapnel object at the bomb's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.shrapnel_color

        self.image = pygame.Surface((self.settings.shrapnel_width, self.settings.shrapnel_height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = bomb.rect.midbottom

        #Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

        #Shrapnel direction
        self.direction = direction

    def update(self):
        """Move the shrapnel across the screen."""
        #Update the decimal position of the shrapnel.
        self.x += self.settings.shrapnel_speed * self.direction
        #Update the rect position
        self.rect.x = self.x

        #Remove shrapnel that reaches the edge of the screen
        screen_rect = self.screen.get_rect()
        if not screen_rect.colliderect(self.rect):
            self.kill()

    def draw_shrapnel(self):
        """Draw the shrapnel to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)