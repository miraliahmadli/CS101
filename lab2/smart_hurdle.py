import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/hurdles3.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def jump():
    hubo.turn_left()
    while not hubo.right_is_clear():
        if hubo.on_beeper():
            return
        hubo.move()

    if hubo.on_beeper():
        return
    turn_right()
    hubo.move()
    turn_right()

    while hubo.front_is_clear():
        if hubo.on_beeper():
            return
        hubo.move()
    hubo.turn_left()


def hurdle():
    while hubo.front_is_clear() and (not hubo.on_beeper()):
        hubo.move()
    while not hubo.on_beeper():
        jump()
        while hubo.front_is_clear() and (not hubo.on_beeper()):
            hubo.move()

hurdle()
