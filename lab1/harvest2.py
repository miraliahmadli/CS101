import sys
sys.path.append("//Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def pick_and_go():
    if hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


def go_to_next_diamond():
    hubo.move()
    hubo.turn_left()
    hubo.move()


def harvest():
    for i in range(5, -1, -2):
        for _ in range(3):
            for _ in range(i):
                pick_and_go()
            hubo.turn_left()
        for _ in range(i-1):
            pick_and_go()
        if hubo.on_beeper():
            hubo.pick_beeper()
        if i == 1:
            break
        go_to_next_diamond()


hubo.turn_left()
for _ in range(6):
    hubo.move()
turn_right()
harvest()
