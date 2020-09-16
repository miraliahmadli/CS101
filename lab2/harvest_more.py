import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def pcik_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()


def right_turn():
    turn_right()
    hubo.move()
    turn_right()


def left_turn():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()


def harvest(is_right_turn=False):
    for _ in range(5):
        pcik_beeper()
        hubo.move()
    if is_right_turn:
        pcik_beeper()
        right_turn()
    else:
        pcik_beeper()
        left_turn()


hubo.move()
is_right_turn = False
for _ in range(6):
    harvest(is_right_turn)
    is_right_turn = not is_right_turn
