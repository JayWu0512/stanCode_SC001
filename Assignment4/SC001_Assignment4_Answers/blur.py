"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: old image
    :return: new image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # Todo: get pixel of new_img at x,y
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                a = img.get_pixel(x, y)
                b = img.get_pixel(x+1, y)
                c = img.get_pixel(x, y+1)
                d = img.get_pixel(x+1, y+1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red) / 4
                pixel.green = (a.green + b.green + c.green + d.green) / 4
                pixel.blue = (a.blue + b.blue + c.blue + d.blue) / 4
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                a = img.get_pixel(x-1, y)
                b = img.get_pixel(x, y)
                c = img.get_pixel(x-1, y+1)
                d = img.get_pixel(x, y+1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red) / 4
                pixel.green = (a.green + b.green + c.green + d.green) / 4
                pixel.blue = (a.blue + b.blue + c.blue + d.blue) / 4
            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                a = img.get_pixel(x, y-1)
                b = img.get_pixel(x+1, y)
                c = img.get_pixel(x, y)
                d = img.get_pixel(x+1, y-1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red) / 4
                pixel.green = (a.green + b.green + c.green + d.green) / 4
                pixel.blue = (a.blue + b.blue + c.blue + d.blue) / 4
            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                a = img.get_pixel(x-1, y-1)
                b = img.get_pixel(x, y-1)
                c = img.get_pixel(x-1, y)
                d = img.get_pixel(x, y)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red) / 4
                pixel.green = (a.green + b.green + c.green + d.green) / 4
                pixel.blue = (a.blue + b.blue + c.blue + d.blue) / 4
            elif y == 0:
                # Get top edge's pixels (without two corners)
                a = img.get_pixel(x-1, y)
                b = img.get_pixel(x+1, y)
                c = img.get_pixel(x, y)
                d = img.get_pixel(x-1, y+1)
                e = img.get_pixel(x+1, y+1)
                f = img.get_pixel(x, y+1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red + e.red + f.red) / 6
                pixel.green = (a.green + b.green + c.green + d.green + e.green + f.green) / 6
                pixel.blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue) / 6
            elif y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                a = img.get_pixel(x, y-1)
                b = img.get_pixel(x+1, y-1)
                c = img.get_pixel(x-1, y-1)
                d = img.get_pixel(x, y)
                e = img.get_pixel(x+1, y)
                f = img.get_pixel(x-1, y)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red + e.red + f.red) / 6
                pixel.green = (a.green + b.green + c.green + d.green + e.green + f.green) / 6
                pixel.blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue) / 6
            elif x == 0:
                # Get left edge's pixels (without two corners)
                a = img.get_pixel(x, y-1)
                b = img.get_pixel(x, y+1)
                c = img.get_pixel(x+1, y+1)
                d = img.get_pixel(x+1, y-1)
                e = img.get_pixel(x+1, y)
                f = img.get_pixel(x, y)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red + e.red + f.red) / 6
                pixel.green = (a.green + b.green + c.green + d.green + e.green + f.green) / 6
                pixel.blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue) / 6
            elif x == img.width-1:
                # Get right edge's pixels (without two corners)
                a = img.get_pixel(x, y)
                b = img.get_pixel(x-1, y-1)
                c = img.get_pixel(x, y-1)
                d = img.get_pixel(x-1, y)
                e = img.get_pixel(x-1, y+1)
                f = img.get_pixel(x, y+1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red + e.red + f.red) / 6
                pixel.green = (a.green + b.green + c.green + d.green + e.green + f.green) / 6
                pixel.blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue) / 6
            else:
                # Inner pixels.
                a = img.get_pixel(x-1, y-1)
                b = img.get_pixel(x, y-1)
                c = img.get_pixel(x+1, y-1)
                d = img.get_pixel(x-1, y)
                e = img.get_pixel(x, y)
                f = img.get_pixel(x+1, y)
                g = img.get_pixel(x-1, y+1)
                h = img.get_pixel(x, y+1)
                i = img.get_pixel(x+1, y+1)
                pixel = new_img.get_pixel(x, y)
                pixel.red = (a.red + b.red + c.red + d.red + e.red + f.red + g.red + h.red + i.red) / 9
                pixel.green = (a.green + b.green + c.green + d.green + e.green + f.green + g.green + h.green + i.green) / 9
                pixel.blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue + g.blue + h.blue + i.blue) / 9
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
