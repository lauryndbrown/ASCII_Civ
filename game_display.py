from input_tools import *
class Display:
    def game_screen(self, game, player_1, player_2):
        pass
    def scores(self, game, player_1, player_2):
        pass
    def board(self, player_1, player_2):
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

