from game_display import Display
from input_tools import *
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
          
