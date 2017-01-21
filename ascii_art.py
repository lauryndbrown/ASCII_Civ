from PIL import Image
from os import sys
class ASCII_Art:
    """
    Library to convert an image to ASCII
    """
    def __init__(self, chars):
        """
        Assumes chars is sorted from lightest to darkest value
        """
        self.chars = chars
    def image_to_ascii(self, image):
        """
        Given an image converts to ASCII Art
        """
        image = self.to_greyscale(image)
        image = self.scale_image(image)
        ascii_chars = self.pixels_to_ascii(image)
        return ''.join(ascii_chars)
        #image.show()

    def scale_image(self, image, width=100):
        """
        Scales an image
        """
        return image
    def to_greyscale(self, image):
        """
        Converts an image to greyscale
        """
        return image.convert('L')
    def pixels_to_ascii(self, image, row_incr=4, col_incr=5):
        """
        Converts the individual pixels to ascii
        """
        ascii_img = []
        #[self.char[pixel] for pixel in image.getdata()]
        row = 0
        col = 0
        height, width = image.size
        for row in range(0, height, row_incr):
            for col in range(0, width, col_incr):
                row_end = row+row_incr
                col_end = col+col_incr
                if row_end>=height:
                    row_end = height-1
                if col_end>=width:
                    col_end = width-1
                ascii_char = self.convert_pixel_block(image,row,row_end,col,col_end)
                ascii_img.append(ascii_char)
            ascii_img.append('\n')
        return ascii_img
    def convert_pixel_block(self, image, row_start, row_end, col_start, col_end):
        """

        """
        def get_pixel_block(image, row_start, row_end, col_start, col_end ):
            """
            Returns a block of pixels
            """
            pixel_block = []
            for x in range(row_start, row_end):
                for y in range(col_start, col_end):
                    try:
                        pixel_block.append(image.getpixel((x,y)))
                    except: 
                        print("X:"+str(x)+" Y:"+str(y))
                        print("Width:"+str(image.size[0])+" Height:"+str(image.size[1]))
                        image.show()
                        exit(1)
            return pixel_block
        def calc_avg_pixel(pixels):
            """
            Given: a list of greyscale pixels
            Return: Calcuted pixel average (rounded)
            """
            total= 0
            for pixel in pixels:
                total+=pixel
            if total==0:
                return 0
            return int(total/len(pixels))
        pixel_block = get_pixel_block(image, row_start, row_end, col_start, col_end)
       # print("Row - Start:"+str(row_start)+" End:"+str(row_end))
       # print("Col - Start:"+str(col_start)+" End:"+str(col_end))
       # print("Width:"+str(image.size[0])+" Height:"+str(image.size[1]))
       # print(str(pixel_block))
       # print()
        avg_pixel = calc_avg_pixel(pixel_block)
        return self.pixel_to_ascii(avg_pixel)
    def pixel_to_ascii(self, pixel):
        """
        Return ascii value for a given pixel
        """
        #pixel/Max_Pixel
        pixel_index = int(pixel/255)
        #Multiplied by the number of characters
        pixel_index *=len(self.chars)-1 
        #You would also add the min possible pixel if it were not zero
        return self.chars[pixel_index]
if __name__=="__main__":
    chars = list('.,*:+?S%@#')
    img_converter = ASCII_Art(chars)
    image = Image.open(sys.argv[1])
    ascii_img = img_converter.image_to_ascii(image)
    print(ascii_img)
