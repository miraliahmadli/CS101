from math import *
import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1media import *


img = load_picture("./images/ironman.jpg" )
direction = input("Input the direction: ")
angle = int(input("Skewing angle: "))

#----------------------------------------------------------#
#
# Function skew
#
# Input:
#		img: loaded image
#		direction: vertical or horizontal
#		angle: -89 to 89 degrees
#
# Output:
#		new_img: skewed image
#		print “Wrong input!!!” if inputs are not in range
#
#----------------------------------------------------------#
def calc_skewing(w, h, x, y, skew, direc):
    if direc == "vertical":
        if skew > 0:
            return int(x + (h - y)*skew), y
        else:
            return int(x - y*skew), y
    else:
        if skew > 0:
            return x, int(y + (w - x)*skew)
        else:
            return x, int(y - x*skew)


def skew(img, direction, angle):
	#implement here
    w,h = img.size()
    if not (-89 <= angle <= 89):
        print("Wrong Input")
        return

    rad = angle * pi / 180
    skewing = tan(rad)
    if direction != "vertical" and direction != "horizontal":
        print("Wrong Direction")
        return
    
    new_w, new_h = calc_skewing(2*w, 2*h, w, h, abs(skewing), direction)
    new_img = create_picture(new_w, new_h)
    black = (0, 0, 0)
    for x in range(w):
        for y in range(h):
            color = img.get(x, y)
            nx, ny = calc_skewing(w, h, x, y, skewing, direction)
            new_img.set(nx, ny, color)
    new_img.show()

# direction = "horizontal"
# angle = 30
skew(img, direction, angle)
