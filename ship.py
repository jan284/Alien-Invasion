import os
import pygame 


class Ship:
    """Class to manage ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship's image
        images = os.chdir('[REDACTED]')
        self.image = pygame.image.load('rocket_ship.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """Update ship's position based on movement flag"""
        #Update ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update ship's position
        self.rect.x = self.x
    
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)