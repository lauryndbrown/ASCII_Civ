"""
Beginning as a Utopia-like Game with (hopefully) some clever ASCII art.

Writen by Lauryn D. Brown 
"""
import sys

from input_tools import * 
from ascii_game import Game
from player import Player
from civ_display import CivDisplay

class Citizen:
    """
    
    """
    def __init__(self, nation, happiness, health):
        self.nation = nation
        self.happiness = happiness
        self.health = health
class Building:
    """
    """
    def __init__(self, name, building_type):
        self.name = name
        self.building_type = building_type
class City:
    """
    """
    def __init__(self, name, citizens=[], buildings=[]):
        self.name = name
        self.citizens = citizens
        self.buildings = buildings
    def add_citizen(self, citizen):
        if citizen not in self.citizens:
            self.citizens.append(citizen)
    def remove_citizen(self, citizen):
        if citizen in self.citizens:
            self.citizens.remove(citizen)
    def add_building(self, building):
        if building not in self.buildings:
            self.buildings.append(building)
    def remove_building(self, building):
        if building in self.buildings:
            self.buildings.remove(building)
class Nation:
    """
    """
    def __init__(self, name, wealth=100, cities=[]):
        self.name = name
        self.wealth = wealth
        self.cities = cities
    def add_city(self, cities):
        if city not in self.cities:
            self.cities.append(city)
    def remove_city(self, city):
        if city in self.city:
            self.cities.remove(city)
    def cities_names(self):
        return [city.name for city in self.cities]
    def __str__(self):
        return "Name: "+self.name+" Wealth:"+str(self.wealth)+"\nCities:"+str(self.cities_names())
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
    @property
    def nation(self):
        return self._nation
    @nation.setter
    def nation(self, nation):
        self._nation = nation
        self.score =  self._nation.wealth
class Choice:
    def __init__(self, name, method, args):
        self.name = name
        self.method = method
        #args should be a tuple
        if args==None:
            self.args = ()
        else:
            self.args = args


class CivGame(Game):
    IMAGE_PATH = "Images/"
    GAME_SCREEN = 1
    SETTINGS_SCREEN = 2
    NATION_SCREEN = 3
    BUILD_SCREEN = 4
    def __init__(self, display, player_1, player_2):
        super().__init__(display, player_1, player_2)
        self.choices = []
        self.choices.append(Choice("End Game",self.end_game, None))
        self.choices.append(Choice("Settings",self.display.settings_screen, (self,)))
        self.choices.append(Choice("Nation Details",self.display.nation_screen, (self,)))
        self.choices.append(Choice("Build",self.display.build_screen, (self,)))

    def tick(self):
        choice = enter_next_action("Enter next action: ", self.choices)
        choice.method(*tuple(choice.args))
        return choice.method!=self.end_game

    def end_game(self):
        pass
def create_new_game(display):
    #Get Names for Player 1
    player_1_name = are_you_sure("What's your name? ")
    nation_1_name = are_you_sure("What will you name your nation? ")
    #Create Nations for Both Players
    nation_1 = Nation(nation_1_name)
    nation_2 = Nation(CivPlayer.DEFAULT_OPPONENT_NATION)
    #Create both players
    player_1 = CivPlayer(player_1_name,nation_1)
    player_2 = CivPlayer(CivPlayer.DEFAULT_OPPONENT_NAME, nation_2)
    #Create Game
    return CivGame(display, player_1, player_2)
def load_saved_game(display):
    #removed and actually write the function
    return create_new_game(display)

def main(argv):
    display = CivDisplay()
    is_new_game = display.start_menu()
    if is_new_game: 
        game = create_new_game(display)
    else:
        game = load_saved_game(display)
    game.start()
    print("End Game")
if __name__=="__main__":
   # main(sys.argv)
   nation1 = Nation("Nation1")
   nation2 = Nation("Nation2")
   player1 = CivPlayer("Player1", nation1)
   player2 = CivPlayer("Player2",nation2)
   
   display = CivDisplay()
   game = CivGame(display,player1,player2)
   game.start()

