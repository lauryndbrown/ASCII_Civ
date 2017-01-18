from abc import ABC, abstractmethod
from player import Player
from input_tools import *
class Game(ABC):
    """
    Generic Abstract Game Class
    """
    END_GAME = 0
    COMPUTER_NAME = "Computer"
    def __init__(self, display, player_1, player_2, start_day=0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.day = start_day
        self.display = display

    def start(self):
        """
        Plays the game. While still_playing is True keep playing.
        Note that it calls abstract method self.tick(). 
        """
        print("The Game Begins!") #Should be done by display
        still_playing = True
        while still_playing:
            still_playing = self.tick() 

    @abstractmethod
    def tick(self):
        """
        MUST be extended to return Boolean value for 
        still_playing in start function
        """
        self.display.game_screen(self,self.player_1,self.player_2)

    def next_action(self, action):
        if action == Game.END_GAME:
            self.save_game()
            return False
        return True

    def save_game(self):
         pass
