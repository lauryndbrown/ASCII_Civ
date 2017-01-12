from player import Player
from input_tools import *
class Game:
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
        Begin the Game
        """
        print("The Game Begins!")
        still_playing = True
        while still_playing:
            still_playing = self.tick() 

    def tick(self):
        """
        MUST be extended to return some value for 
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

    def settings_menu(self):
        """
        Prints the settings menu Screen to the player
        """
        print("Settings Menu")
    def game(self):
        """
        Prints the game 
        """
        print("Game")

