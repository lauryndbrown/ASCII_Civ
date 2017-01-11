"""
Beginning as a Utopia-like Game with (hopefully) some clever
ASCII art.

Writen by Lauryn D. Brown 
"""

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
    def __init__(self, name, nation, citizens):
        self.name = name
        self.nation = nation
        self.citizens = citizens
class Nation:
    """
    """
    def __init__(self, name, wealth, cities):
        self.name = name
        self.wealth = wealth
        self.cities = cities
class Player:
    """
    """
    def __init__(self, name, high_score=0, nations=[]):
        self.name = name
        self.high_score = high_score
        self.nations = nations
    def add_nation(self, nation):
        if nation not in self.nations:
            self.nations.append(nation)
    def remove_nation(self, nation):
        if nation in self.nations:
            self.nations.remove(nation)
class Game:
    """
    Logic wrapper for the overall game
    """
    YES = "Y"
    NO = "N"
    YES_OR_NO = {YES:True,NO:False}
    COMPUTER_NAME = "computer"
    def __init__(self, first_player, second_player=COMPUTER_NAME, start_day=0):
        self.first_player = first_player
        self.second_player = second_player
        self.day = start_day

    def start(self):
        """
        Begin the Game
        """
        print("The Game Begins!")
        still_playing = True
        while still_playing:
            still_playing = Game.yes_or_no("Do you want to Continue?[Y/N] ")
            if still_playing:
                print("Playing")
            else:
                self.save_game()
    def save_game(self):
        pass

    def start_menu():
        """
        Prints out the Start Menu Screen to to player
        """
        print("Welcome to ASCII Civ")
        new_game = Game.yes_or_no("Do you want to play a New Game?[Y/N] ")
        if new_game:
            print("New Game")
        else:#TODO:check if previous game exists
            print("Last Saved Game")
        return new_game
    def yes_or_no(message):
        """
        Helper Function that handles user input for yes or no questions
        """
        while True:
            response = input(message)
            if response==Game.YES or response==Game.NO:
                return Game.YES_OR_NO[response]
        
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
        player = Player(input("What's your name? "))
        game = Game(player)
        game.start()
    else:
        #TODO: Add functionality for loading last saved game
        pass
    print("End Game")
if __name__=="__main__":
    main(sys.argv)

