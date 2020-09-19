import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world(filename="./worlds/trash3.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.turn_left()

def turn_right():
    for _ in range(3):
        hubo.turn_left()


def right_turn():
    turn_right()
    try:
        hubo.move()
    except:
        return False
    turn_right()
    return True


def left_turn():
    hubo.turn_left()
    try:
        hubo.move()
    except:
        return False
    hubo.turn_left()
    return True


def move():
    pcik_beeper()
    while hubo.front_is_clear():
        hubo.move()
        pcik_beeper()


def face_east():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()


def pcik_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()


def drop_beeper():
    while hubo.carries_beepers():
        hubo.drop_beeper()


def zigzag(is_right_turn=True):
    move()
    if is_right_turn:
        succ = right_turn()
    else:
        succ = left_turn()
    if succ:
        zigzag(not is_right_turn)


def go_back():
    face_east()
    move()
    hubo.turn_left()
    move()
    hubo.turn_left()

zigzag()
face_east()
go_back()
drop_beeper()
