import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to Manage game assests and behaviour"""

    def __init__(self):
        # Initialise the game, and create game resources.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        # Watch for keybord and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
                     

    def _check_keydown_event(self,event):
        #Respond to key presses.
        if event.key == pygame.K_RIGHT:
            #   Move the ship to right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #   Move the ship to left.
            self.ship.moving_left = True

    def _check_keyup_event(self,event):
        #Respond to key presses.
        if event.key == pygame.K_RIGHT:
            #   Move the ship moving to right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #   Stop the ship moving to left.
            self.ship.moving_left = False

    def _update_screen(self):
         # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recent drawn screen visible
            pygame.display.flip()

    def run_game(self):
        # Start the main loop for the game

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance, and run the game

    ai = AlienInvasion()
    ai.run_game()       