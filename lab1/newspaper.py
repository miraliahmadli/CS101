import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/newspaper.wld")

hubo = Robot(beepers=1)
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    if hubo.front_is_clear():
        hubo.move()


def newspaper():
    for _ in range(4):
        jump()
    
    hubo.drop_beeper()
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.move()

    for _ in range(4):
        jump()
    
hubo.move()
newspaper()
