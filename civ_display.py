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
        print("{:10} {:{col}} {:{col}}".format("Player: ", player_1.name, player_2.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Nation: ",player_1.nation.name, player_2.nation.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Wealth: ", str(player_2.nation.wealth), str(player_2.nation.wealth), col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Cities: ", str(len(player_2.nation.cities)), str(len(player_2.nation.cities)), col=self.col_size)) 

    def in_game_menu(self):
        print("Action[1]"+self.TAB+"Action[2]"+self.TAB+"End Game[0]")
          
    def settings_menu(self):
        print(Settings)
if __name__=="__main__":
   from civ_game import *
   nation1 = Nation("Nation1")
   nation2 = Nation("Nation2")
   player1 = CivPlayer("Player1", nation1)
   player2 = CivPlayer("Player2",nation2)
   
   display = CivDisplay()
   display.board(player1, player2)
