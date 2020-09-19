import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/trash2.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def pcik_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()


def drop_beeper():
    while hubo.carries_beepers():
        hubo.drop_beeper()


def trash():
    pcik_beeper()
    while hubo.front_is_clear():
        hubo.move()
        pcik_beeper()
    
    hubo.turn_left()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    
    turn_right()
    hubo.move()

    drop_beeper()


trash()