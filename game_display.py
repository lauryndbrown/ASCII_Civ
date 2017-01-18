from PIL import Image
from abc import ABC, abstractmethod
from input_tools import *
class Display(ABC):
    @abstractmethod
    def game_screen(self, game, player_1, player_2):
        pass
    def start_menu(self, welcome_str):
        """
        Prints out the Start Menu Screen to to player
        """
        print(welcome_str)
        new_game = yes_or_no("Do you want to play a New Game?[Y/N] ")
        if new_game:
            print("New Game")
        else:
            print("Last Saved Game")
        return new_game
    @abstractmethod
    def settings_menu(self):
        """
        Prints the settings menu Screen to the player
        """
        pass
    
    def image_to_ascii(self, path):
        """
        """
        image = Image.open(path)
        image.show()
