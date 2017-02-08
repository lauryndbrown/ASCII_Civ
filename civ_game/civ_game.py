"""
Beginning as a Utopia-like Game with (hopefully) some clever ASCII art.

Writen by Lauryn D. Brown 
"""
import sys
from civ_game.civ_display import CivDisplay
from civ_game.game_entities import *
from ascii_game.game import Game, Choice
from ascii_game.player import Player
class CivPlayer(Player):
    """
    Player specific to the CivGame class
    """
    DEFAULT_OPPONENT_NAME = "Flick" 
    DEFAULT_OPPONENT_NATION = "Utopia"

    def __init__(self, name, nation):
        self.name = name
        self._nation = nation
        self.score = 0
        self.high_score = 0
        self.selected_city = None
    @property
    def nation(self):
        return self._nation
    @nation.setter
    def nation(self, nation):
        self._nation = nation
        self.score =  self._nation.wealth

class CivGame(Game):
    """
    Game Class Specific to the Civilization Game
    """
    #Menu Names
    GAME_MENU = "Game"
    SETTINGS_MENU = "Settings"
    NATION_MENU = "Nation"
    BUILD_MENU = "Build"
    #Option Names
    BACK_OPTION = "Back"
    def __init__(self, display, player_1, player_2):
        """
        Initializes the CivGame class 
        Builds the Game Menus
        """
        super().__init__(display, player_1, player_2)
        game_menu = []
        settings_menu = []
        nation_menu = []
        build_menu = []
        #Game Menu
        game_menu.append(Choice("End Game",self.end_game, None, None))
        game_menu.append(Choice("Settings",self.display.settings_screen, (self,), self.SETTINGS_MENU))
        game_menu.append(Choice("Nation Details",self.display.nation_screen, (self,), self.NATION_MENU))
        game_menu.append(Choice("Build",self.display.build_screen, (self,), self.BUILD_MENU))
        #Settings Menu
        settings_menu.append(Choice(self.BACK_OPTION,self.display.game_screen, (self,), self.GAME_MENU))
        #Nation Details Menu
        nation_menu.append(Choice(self.BACK_OPTION,self.display.game_screen, (self,), self.GAME_MENU))
        #Build Menu
        build_menu.append(Choice(self.BACK_OPTION,self.display.game_screen, (self,), self.GAME_MENU))
        build_menu.append(Choice("New City",self.display.build_screen, (self,), None))
        build_menu.append(Choice("Residentail Buildings",self.display.build_screen, (self,), None))
        build_menu.append(Choice("Food Buildings",self.display.build_screen, (self,), None))
        build_menu.append(Choice("Equipment Buildings",self.display.build_screen, (self,), None))
        build_menu.append(Choice("Community Buildings",self.display.build_screen, (self,), None))
        self.menus = {self.GAME_MENU:game_menu, self.SETTINGS_MENU:settings_menu,self.NATION_MENU:nation_menu, self.BUILD_MENU:build_menu}
    
        #Current game menu is pointed to by self.menu
        self.menu = game_menu
        #Because the game has just started the previous menu is None
        self.prev_menu = None
        self.day = 0
       
    def end_game(self):
        """
        Method Called when the game ends
        """
        pass
def create_new_game(display):
    """
    Creates a New CivGame complete with the players
    Prompts the user to name their Player and their Nation
    """
    player_1_name, nation_1_name, city_1_name = display.ask_player_details()
    #Create Nations for Both Players
    nation_1 = Nation(nation_1_name)
    city_1 = City(city_1_name)
    nation_1.add_city(city_1)
    nation_2 = Nation(CivPlayer.DEFAULT_OPPONENT_NATION)
    #Create both players
    player_1 = CivPlayer(player_1_name,nation_1)
    player_1.selected_city = city_1
    player_2 = CivPlayer(CivPlayer.DEFAULT_OPPONENT_NAME, nation_2)
    #Create Game
    game = CivGame(display, player_1, player_2)
    return game
def load_saved_game(display):
    """
    Loads Saved Game from File
    """
    #removed and actually write the function
    return create_new_game(display)

def main(argv):
    """
    Plays the Game complete with the introduction
    """
    display = CivDisplay()
    is_new_game = display.start_menu()
    if is_new_game: 
        game = create_new_game(display)
    else:
        game = load_saved_game(display)
    game.start()
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=='N':
        """
        Plays the game no introduction
        """
        nation1 = Nation("Nation1")
        city_1 = City("City1")
        nation1.add_city(city_1)
        nation2 = Nation("Nation2")
        player1 = CivPlayer("Player1", nation1)
        player1.selected_city = city_1
        player2 = CivPlayer("Player2",nation2)
        display = CivDisplay()
        game = CivGame(display,player1,player2)
        game.start()
    else:
        main(sys.argv)

