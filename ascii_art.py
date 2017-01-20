class ASCII_Art:
    """
    Library to convert an image to ASCII
    """
    def __init__(self, chars):
        """"
        """"
        self.chars = chars
    def open_image(self, path):
        """
        Opens an image at the given path
        """
        image = Image.open(path)
        return image

    def image_to_ascii(self, image):
        """
        Given an image converts to ASCII Art
        """
        image = self.to_greyscale(image)
        image = self.scale_image(image)
        ascii_chars = self.pixels_to_ascii(image)
        return ''.join(ascii_chars)
        #image.show()

    def scale_image(self, image, width):
        """
        Scales an image
        """"

        return image
    def to_greyscale(self, image):
        """
        Converts an image to greyscale
        """"
        return image.convert('L')
    def pixels_to_ascii(self, image, row_incr, col_incr):
        """"
        Converts the individual pixels to ascii
        """"
        ascii_img = []
        #[self.char[pixel] for pixel in image.getdata()]
        row = 0
        col = 0
        width, height = image.size
        for row in range(0, height, row_incr):
            for col in range(0, width, col_incr):
                ascii_img.append(self.pixel_to_ascii(pixel))
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
                    pixel_block.append(image.getpixel((x,y)))
            return pixel_block
        def calc_avg_pixel(pixels):
            """
            Given: a list of greyscale pixels
            Return: Calcuted pixel average (rounded)
            """
            total= 0
            for pixel in pixels:
                total+=pixel
            return int(total/len(pixels))
        pixel_block = get_pixel_block(image, row_start, row_end, col_start, col_end)
        avg_pixel = calc_avg_pixel(pixel_block)
        return self.pixel_to_ascii(avg_pixel)
    def pixel_to_ascii(self, pixel)
        """"
        Return ascii value for a given pixel
        """"
        pixel_index = 0#some conversion between pixel and char
        return self.char[pixel_index]
if __name__=="__main__":
    chars = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
    img_converter = ASCII_Art(chars)
    ascii_img = img_converter.image_to_ascii(sys.argv)
    print(ascii_img)
