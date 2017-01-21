#ASCII Based Game built in Python
This ascii-based civilization building game is built with only Pillow as a dependency. It is meant to run in the command line, and uses ascii art for all its graphics. It is a work in progress. See Progress section for current status. 
##Progress
Currently, the graphics are in place for the game. While the game itself has yet to be implemented. The ascii library in particular is very usable and easy to get started with. Features upcomming include civ-game-play, loading saved games, and graphics specific to the civ-game.
##Getting up and Running
The Game is built with Python3 and uses the Python library Pillow.
`pip install pillow`
###Running the Game 
`python civ-game.py`
Note that the civ-game.py has an optional command-line argument to skip the intro text. This is useful for debugging. Simply add N as an argument as so: `python civ-game.py N`.
###ASCII Game
The ASCII Game Class located in `ascii_game.py` can be extended to leverage the other features and create terminal-based games.
```
from ascii_game.py import ASCII_Game
class YourClass(ASCII_Game):

  def __init(self, display, player_1, player_2):
      # your code here
```
Notice that a display is required to separate the game logic from the code printing to the terminal. You display should extend the Display class in game_display.py.  
###Image to ASCII Conversion
The ASCII_Art Class located in `ascii_art.py` is an image converter that takes a PIL Image and converts it to ASCII characters that can then be printed to the screen. **Examples can be found in the ASCII_Examples folder of the project.** :) It can be used in isolation and has no dependencies with the rest of the project. Usage as shown:
####Via Command Line
The command line version assumes the characters `'#@%S?+:*,. '` to use as conversion.
```
python ascii_art.py path\to\image
```
####Adding to your own Code
Pillow is a dependcy.
```
from ascii_art.py import ASCII_ART
from PIL import Pillow
chars = list('#@%S?+:*,. ')
image = Image.open(sys.argv[1])
img_converter = ASCII_Art(chars)
img_converter.invert_chars()
ascii_img = img_converter.image_to_ascii(image)
print(ascii_img)
```
##Image Sources
- treasureMap.png: https://pixabay.com/en/treasure-map-treasure-hunt-153425/
- flag.jpg: https://pixabay.com/en/flag-blow-wind-flutter-characters-75047/
