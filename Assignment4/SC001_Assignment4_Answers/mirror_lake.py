"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage, the original image
    :return: mirror lake
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            colored_p = img.get_pixel(x, y)

            blank1 = b_img.get_pixel(x, y)
            blank2 = b_img.get_pixel(x, b_img.height - 1 - y)

            blank1.red = colored_p.red
            blank1.green = colored_p.green
            blank1.blue = colored_p.blue

            blank2.red = colored_p.red
            blank2.green = colored_p.green
            blank2.blue = colored_p.blue
    return b_img


def main():
    """
    Step 1: show initial image
    Step 2: show mirror lake
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
