from ascii_art import ASCII_Art 
from PIL import Image
from game_display import Display
from input_tools import *
from subprocess import call
import os
class CivDisplay(Display):
    """
    ASCII Art for game
    """
    #Commonly Used characters for Horizontal Rule
    HR_BOLD = "="
    HR_DASHED = '-'
    HR_LIGHT = '_'
    #Images Directory
    IMAGES = "Images\\"    
    CHARS = list('#@%S?+:*,. ')
    #Offsets used to determine the whitespace needed to fill the screen
    TITLE_OFFSET = 3
    IN_GAME_MENU_OFFSET = 4
    GAME_SCREEN_OFFSET = 6 + TITLE_OFFSET + IN_GAME_MENU_OFFSET 
    SETTINGS_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    NATION_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    BUILD_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET

    def __init__(self, col_size=50):
        super().__init__(col_size)
        self.last_screen_method = None
        self.img_converter = ASCII_Art(self.CHARS)


    def start_menu(self):
        """
        Displays Welcome Message when Game Starts
        """
        image = Image.open(self.IMAGES+"title.png")
        ascii_img = self.img_converter.image_to_ascii(image, 300)
        print(self.center("ASCII CIV", self.HR_BOLD))
        print(ascii_img, end="")
        print(self.format_HR(' '))
        message = self.format_HR(' ', int(os.get_terminal_size().columns/4))+"Do you want to play a New Game?[Y/N] "
        new_game = yes_or_no(message)
        if new_game:
            print("New Game")
        else:
            print("Feature not Yet Implemented. Creating New Game")
            #print("Last Saved Game")
        return new_game
        self.last_menu = (self.start_menu, ())

    def game_screen(self, game):
        """
        Displays all information to the screen during a game
        """
        self.clear_screen()
        print(self.center("ASCII CIV", self.HR_BOLD))
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
        print(self.center("Day "+str(game.day), ' '))
        print("{:10} {:{col}} {:{col}}".format("Player: ", game.player_1.name, game.player_2.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Nation: ",game.player_1.nation.name, game.player_2.nation.name, col=self.col_size)) 
        print("{:10} {:{col}} {:{col}}".format("Wealth: ", str(game.player_2.nation.wealth), str(game.player_2.nation.wealth), col=self.col_size)) 

    def _board(self, player_1, player_2):
        print("{:10} {:{col}} {:{col}}".format("Cities: ", str(len(player_2.nation.cities)), str(len(player_2.nation.cities)), col=self.col_size)) 

    def _in_game_menu(self, choices):
        """
        Private method to display the in-game menu choices
        """
        menu_str = ""
        for index in range(len(choices)):
            choice_str = "{}[{}]".format(choices[index].name,index)
            menu_str+="{}     ".format(choice_str)
        print(self.center("Menu", self.HR_DASHED))
        print(self.center(menu_str, ' '))

          
    def settings_screen(self, game):
        """
        Settings Screen
        """
        self.clear_screen()
        print(self.center("SETTINGS", self.HR_BOLD))
        self.fill_screen(self.SETTINGS_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.settings_screen, (game,))

    def nation_screen(self, game):
        """
        Nation Details Screen
        """
        self.clear_screen()
        print(self.center("NATION DETAILS", self.HR_BOLD))
        self.fill_screen(self.NATION_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.nation_screen, (game,))

    def build_screen(self, game):
        """
        Build Screen
        """
        self.clear_screen()
        print(self.center("BUILD", self.HR_BOLD))
        self.fill_screen(self.BUILD_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.build_screen, (game,))
    def end_game(self):
        """
        Message shown when the game exits
        """
        print("End Game")

    def center(self, message, border, size=os.get_terminal_size().columns):
        """
        Returns a string with message centered between characters of a given border
        """
        return message.center(size, border)
    
    def format_HR(self, border, size=os.get_terminal_size().columns-1):
        """
        Returns a Horizontal Rule of length size
        """
        return border*size
    def clear_screen(self):
        """
        Clears the Screen
        """
        print()
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
