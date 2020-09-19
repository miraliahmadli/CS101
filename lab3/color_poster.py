import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1media import *

# This code converts an image into a black & white poster.

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

image = load_picture('./images/panda.png')
width, height = image.size()

def turn_bw(image, width, height):
    for y in range(height):
        for x in range(width):
            r, g, b = image.get(x, y)
            average_brightness = (r + g + b) // 3
            if average_brightness > threshold:
                image.set(x, y, white)
            else:
                image.set(x, y, black)
                
    image.show()

def turn_colors(image, width, height):
    thr_bright = 170
    thr_dark = 70
    for y in range(height):
        for x in range(width):
            r, g, b = image.get(x, y)
            average_brightness = (r + g + b) // 3
            if average_brightness > thr_bright:
                image.set(x, y, yellow)
            elif average_brightness < thr_dark:
                image.set(x, y, blue)
            else:
                image.set(x, y, green)
                
    image.show()

turn_colors(image, width, height)