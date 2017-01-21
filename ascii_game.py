from abc import ABC, abstractmethod
from player import Player
from input_tools import *
class Choice:
    def __init__(self, name, method, args, menu):
        self.name = name
        self.method = method
        #args should be a tuple
        if args==None:
            self.args = ()
        else:
            self.args = args
        self.menu = menu
    def __str__(self):
        return "Name:{} Method:{} Menu:{}".format(self.name,self.method,self.menu)

class Game(ABC):
    """
    Generic Abstract Game Class
    """
    END_GAME = 0
    COMPUTER_NAME = "Computer"
    def __init__(self, display, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.menu = None
        self.prev_menu = None
        self.display = display

    def start(self):
        """
        Plays the game. While still_playing is True keep playing.
        Note that it calls abstract method self.tick(). 
        """
        print("The Game Begins!") #Should be done by display
        self.display.game_screen(self)
        still_playing = True
        while still_playing:
            still_playing = self.tick() 

    def tick(self):
        choice = enter_next_action("Enter next action: ", self.menu, self.display)
        if choice.menu != None:
            self.prev_menu = self.menu
            self.menu = self.menus[choice.menu]
        choice.method(*tuple(choice.args))
        return choice.method!=self.end_game

    def next_action(self, action):
        if action == Game.END_GAME:
            self.save_game()
            return False
        return True

    def save_game(self):
         pass

