import sys

import pygame

from core.settings import Settings
from core.ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Ship constructor needs an instance of AlienInvasion class
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    # In Python, a single leading underscore indicates a helper method.
    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # To access the events that Pygame detects, we’ll use the pygame.event.get() function. This function returns a list of events
        # that have taken place since the last time this function was called.
        # Any keyboard or mouse event will cause this for loop to run.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
