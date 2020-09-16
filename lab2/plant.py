import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/harvest3.wld")

hubo = Robot(beepers=10)
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def drop_beeper():
    if not hubo.on_beeper():
        hubo.drop_beeper()


def right_turn():
    turn_right()
    hubo.move()
    turn_right()


def left_turn():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()


def plant(is_right_turn=False):
    for _ in range(5):
        drop_beeper()
        hubo.move()
    if is_right_turn:
        drop_beeper()
        right_turn()
    else:
        drop_beeper()
        left_turn()


hubo.move()
is_right_turn = False
for _ in range(6):
    plant(is_right_turn)
    is_right_turn = not is_right_turn
