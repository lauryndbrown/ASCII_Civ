from game_display import Display
from input_tools import *
from subprocess import call
import os
class CivDisplay(Display):
    """
    ASCII Art for game
    """
    HR_LENGTH = 100
    TAB = "    "
    HR_BOLD = "="
    HR_DASHED = '-'
    HR_LIGHT = '_'
    
    TITLE_OFFSET = 1
    IN_GAME_MENU_OFFSET = 3
    GAME_SCREEN_OFFSET = 5 + TITLE_OFFSET + IN_GAME_MENU_OFFSET 
    SETTINGS_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    NATION_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    BUILD_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET

    def __init__(self, col_size=50):
        super().__init__(col_size)
        self.hr = '='
        self.last_screen_method = None


    def start_menu(self):
        """
        Displays Welcome Message when Game Starts
        """
        super().start_menu("Welcome to ASCII Civ")
        self.last_menu = (self.start_menu, ())

    def game_screen(self, game):
        """
        Displays all information to the screen during a game
        """
        self.clear_screen()
        self.print_title("ASCII CIV", self.HR_BOLD)
        self._scores(game)
        self._board(game.player_1, game.player_2)
        self.fill_screen(self.GAME_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.game_screen, (game,))

    def reset(self):
        """
        Re-prints the current screen 
        """
        self.last_menu[0](*tuple(self.last_menu[1]))

    def _scores(self, game):
        """
        Private method to display player scores
        """
        self.print_title("Day "+str(game.day), ' ')
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
        self.print_title("Menu", self.HR_DASHED)
        self.print_title(menu_str, ' ')

          
    def settings_screen(self, game):
        self.clear_screen()
        self.print_title("SETTINGS", self.HR_BOLD)
        self.fill_screen(self.SETTINGS_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.settings_screen, (game,))

    def nation_screen(self, game):
        self.clear_screen()
        self.print_title("NATION DETAILS", self.HR_BOLD)
        self.fill_screen(self.NATION_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.nation_screen, (game,))

    def build_screen(self, game):
        self.clear_screen()
        self.print_title("BUILD", self.HR_BOLD)
        self.fill_screen(self.BUILD_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.build_screen, (game,))

    def print_title(self, title, border, size=os.get_terminal_size().columns):
            print(title.center(size, border), end="")

    def print_HR(self, border, size=os.get_terminal_size().columns-1):
        print(border*size)
    def clear_screen(self):
        call(["clear"])
    def fill_screen(self, offset):
        """
        Fills remaining lines of screen with Whitespace
        """
        lines = os.get_terminal_size().lines - 1
        if offset < lines:
            print('\n'*(lines-offset))
if __name__=="__main__":
   from civ_game import *
   nation1 = Nation("Nation1")
   nation2 = Nation("Nation2")
   player1 = CivPlayer("Player1", nation1)
   player2 = CivPlayer("Player2",nation2)
   
   display = CivDisplay()
   game = CivGame(display,player1,player2)

   display.game_screen(game)
