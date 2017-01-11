"""
Beginning as a Utopia-like Game with (hopefully) some clever
ASCII art.

Writen by Lauryn D. Brown 
"""
import game_display as Display
from input_tools import * 
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
class Player:
    """
    """
    def __init__(self, name, high_score=0, nation=None):
        self.name = name
        self.high_score = high_score
        self._nation = nation
        self.score = 0
    @property
    def nation(self):
        return self._nation
    @nation.setter
    def nation(self, nation):
        self._nation = nation
        self.score =  self._nation.wealth

class Game:
    """
    Logic wrapper for the overall game
    """
    END_GAME = 0
    COMPUTER_NAME = "Computer"
    def __init__(self, player_1, player_2=Player(COMPUTER_NAME), start_day=0):
        self.player_1 = player_1
        self.player_2 = player_2
        if player_2.nation==None:
            player_2.nation = Nation("Utopia")
        self.day = start_day

    def start(self):
        """
        Begin the Game
        """
        print("The Game Begins!")
        still_playing = True
        while still_playing:
            if still_playing:
                self.tick()
            still_playing = self.next_action(enter_next_action("Enter next action: ", [0,1,2]))
    def tick(self):
         Display.game_screen(self,self.player_1,self.player_2)
    def next_action(self, action):
        if action == Game.END_GAME:
            self.save_game()
            return False
        return True
    def save_game(self):
         pass

    def start_menu():
        """
        Prints out the Start Menu Screen to to player
        """
        print("Welcome to ASCII Civ")
        new_game = yes_or_no("Do you want to play a New Game?[Y/N] ")
        if new_game:
            print("New Game")
        else:
            print("Last Saved Game")
        return new_game
   
        
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
import sys
def main(argv):
    new_game = Game.start_menu()
    if new_game: 
        player = Player(are_you_sure("What's your name? "))
        nation_name = are_you_sure("What will you name your nation? ")
        player.nation = Nation(nation_name,100)
        game = Game(player)
        game.start()
    else:
        pass
    print("End Game")
if __name__=="__main__":
    main(sys.argv)

