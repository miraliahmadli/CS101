import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/rain2.wld")

hubo = Robot(beepers=100, avenue=2, street=6, orientation='E')
hubo.set_trace("blue")


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def check_window():
    hubo.drop_beeper()
    hubo.move()
    if hubo.right_is_clear():
        hubo.turn_left()
        hubo.turn_left()
        hubo.move()
        hubo.pick_beeper()
        hubo.turn_left()
        hubo.move()


def close_windows():
    while not hubo.on_beeper():
        while hubo.front_is_clear() and not hubo.on_beeper():
            if hubo.right_is_clear():
                check_window()
            else:
                hubo.move()
        hubo.turn_left()
    hubo.pick_beeper()


hubo.move()
turn_right()
hubo.drop_beeper()
hubo.move()
close_windows()
