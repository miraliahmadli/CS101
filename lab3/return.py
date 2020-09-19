import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
create_world()

hubo = Robot(orientation="E", street=5, avenue=5)
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def move():
    while hubo.front_is_clear():
        hubo.move()


def face_east():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()


def go_back():
    face_east()
    move()
    hubo.turn_left()
    move()
    hubo.turn_left()


go_back()
