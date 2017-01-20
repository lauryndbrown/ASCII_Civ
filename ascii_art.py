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
        image = self.scale_image(image)
        image = self.to_greyscale(image)
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
    def pixels_to_ascii(self, image):
        """"
        Converts the individual pixels to ascii
        """"
        ascii_img = []
        return ascii_img
if __name__=="__main__":
    chars = []
    img_converter = ASCII_Art(chars)
    ascii_img = image_to_ascii(sys.argv)
    print(ascii_img)
