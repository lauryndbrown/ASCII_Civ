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
class CivDisplay(Display):
    """
    ASCII Art for game
    """
    HR ="======================"
    TAB = "    "

    def start_menu(self):
        super().start_menu("Welcome to ASCII Civ")

    def game_screen(self, game, player_1, player_2):
        self.scores(game, player_1, player_2)
        self.board(player_1, player_2)
        self.in_game_menu()
    def scores(self, game, player_1, player_2):
        scores = str(player_1.name)+":"+str(player_1.score)
        scores+= self.TAB+str(player_2.name)+":"+str(player_2.score)
        print(self.HR)
        print("Day: "+str(game.day))
        print(scores)
        print('')

    def board(self, player_1, player_2):
        board=str(player_1.nation.name)+self.TAB+str(player_2.nation.name)+"\n"
        board+="Wealth:"+str(player_1.nation)+self.TAB+str(player_2.nation)+"\n"
        print(board)

    def in_game_menu(self):
        print("Action[1]"+self.TAB+"Action[2]"+self.TAB+"End Game[0]")
          
