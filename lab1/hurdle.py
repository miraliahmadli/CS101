import sys
sys.path.append("//Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/hurdles1.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


def hurdle():
    jump()
    while hubo.front_is_clear():
        hubo.move()

    
while hubo.front_is_clear():
    hubo.move()
for _ in range(4):
    hurdle()

hubo.pick_beeper()
