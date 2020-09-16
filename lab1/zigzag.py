import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
create_world()

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


def zigzag(is_right_turn=True):
    while hubo.front_is_clear():
        hubo.move()
    if is_right_turn:
        succ = right_turn()
    else:
        succ = left_turn()
    if succ:
        zigzag(not is_right_turn)

zigzag()
