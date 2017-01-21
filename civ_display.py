from game_display import Display
from input_tools import *
class CivDisplay(Display):
    """
    ASCII Art for game
    """
    HR_LENGTH = 100
    TAB = "    "
    def __init__(self, col_size=50):
        super().__init__(col_size)
        self.hr = ("="*CivDisplay.HR_LENGTH)+"\n"

    def start_menu(self):
        """
        Displays Welcome Message when Game Starts
        """
        super().start_menu("Welcome to ASCII Civ")

    def game_screen(self, game):
        """
        Displays all information to the screen during a game
        """
        print(self.hr)
        self._scores(game)
        print('\n')
        self._board(game.player_1, game.player_2)
        print('\n')
        self._in_game_menu(game.menu)

    def _scores(self, game):
        """
        Private method to display player scores
        """
        print("Day: "+str(game.day))
        print("{:10} {:{col}} {:{col}}".format("Player: ", game.player_1.name, game.player_2.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Nation: ",game.player_1.nation.name, game.player_2.nation.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Wealth: ", str(game.player_2.nation.wealth), str(game.player_2.nation.wealth), col=self.col_size)) 

    def _board(self, player_1, player_2):
        print("{:10} {:{col}} {:{col}}".format("Cities: ", str(len(player_2.nation.cities)), str(len(player_2.nation.cities)), col=self.col_size)) 

    def _in_game_menu(self, choices):
        menu_str = ""
        for index in range(len(choices)):
            choice_str = "{}[{}]".format(choices[index].name,index)
            menu_str+="{}     ".format(choice_str)
        print(menu_str)
          
    def settings_screen(self, game):
        print(self.hr)
        print('Settings')
        self._in_game_menu(game.menu)
        print('\n')
    def nation_screen(self, game):
        print(self.hr)
        print('Nations')
        self._in_game_menu(game.menu)
        print('\n')
    def build_screen(self, game):
        print(self.hr)
        print('Build')
        self._in_game_menu(game.menu)
        print('\n')

if __name__=="__main__":
   from civ_game import *
   nation1 = Nation("Nation1")
   nation2 = Nation("Nation2")
   player1 = CivPlayer("Player1", nation1)
   player2 = CivPlayer("Player2",nation2)
   
   display = CivDisplay()
   game = CivGame(display,player1,player2)

   display.game_screen(game)
