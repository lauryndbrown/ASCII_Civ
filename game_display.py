from PIL import Image
from abc import ABC, abstractmethod
from input_tools import *
import shutil
import os
class Display(ABC):
    PIXEL_BLOCK = (4, 5)
    #list found from http://paulbourke.net/dataformats/asciiart/
    CHARS = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. ')
   # CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
    @abstractmethod
    def game_screen(self, game, player_1, player_2):
        pass
    def start_menu(self, welcome_str):
        """
        Prints out the Start Menu Screen to to player
        """
        print(welcome_str)
        new_game = yes_or_no("Do you want to play a New Game?[Y/N] ")
        if new_game:
            print("New Game")
        else:
            print("Last Saved Game")
        return new_game
    @abstractmethod
    def settings_menu(self):
        """
        Prints the settings menu Screen to the player
        """
        pass
    
    def image_to_ascii(self, path):
        """
        """
        ascii_image = ASCII_Image(path, self.CHARS, (300, 300))
        print(ascii_image.ascii_img)
        ascii_image.image.show()
        


        
    
         
class ASCII_Image:
    ASCII_BLOCK_WIDTH = 4
    ASCII_BLOCK_HEIGHT = 5
    MIN_PIXEL = 0
    MAX_PIXEL = 255
    def __init__(self, path, chars, thumbnail_size):
        self.image = self.prep_image(Image.open(path), thumbnail_size)
        self.path = path
        self.chars = chars
        self.chars_len = len(chars)
        self.pixels = list(self.image.getdata())
        self.ascii_img = self.convert_to_ascii()
    def convert_to_ascii(self):
        ascii_image = []
        index = 0
        row = 0
        width = self.image.size[0]
        col_incr = 4
        row_incr = 1
        while index < len(self.pixels):
            if index > (width-1)+row*width:
                ascii_image.append('\n')
                ascii_image.append(self.pixel_to_char(self.pixels[index]))
                row+=row_incr
                #index+=row*width
            else:
                ascii_image.append(self.pixel_to_char(self.pixels[index]))
                index+= col_incr
        return ''.join(ascii_image)
            

        #converted_pixels = [self.pixel_to_char(self.pixels[index]) for index in range(0, len(self.pixels), 10)]
        #image_ascii = [mean(new_pixels[index : index + 5] for index in range(0,len(pixels),5)]
    def pixel_to_char(self, pixel):
        chars_index = self.MIN_PIXEL+int(pixel/self.MAX_PIXEL*(self.chars_len-1))
        return self.chars[chars_index]
    def prep_image(self, image, size):
        #Make a thumbnail of image
        #image.thumbnail(size)
        new_width = 600
        (original_width, original_height) = image.size
        aspect_ratio = original_height/float(original_width)
        new_height = int(aspect_ratio * new_width)

        image = image.resize((new_width, new_height))

        #Convert to Greyscale
        image = image.convert("L")
        return image
    def convert_pixels(self):
        converted_pixels = self.pixels_to_ascii(self.pixels,self.image.size[0], self.image.size[1])
        ascii_image = [chars[pixel] for pixel in converted_pixels]

if __name__=="__main__":
    from civ_display import CivDisplay
    display = CivDisplay()
    display.image_to_ascii('Images/hack.png')

