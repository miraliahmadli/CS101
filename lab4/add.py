import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
load_world("./worlds/add34.wld")

hubo = Robot()
hubo.set_trace("blue")


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def right_turn():
    turn_right()
    hubo.move()
    turn_right()


def pick_beeper():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
    return cnt


def drop_beeper(n):
    for _ in range(n):
        hubo.drop_beeper()


def add():
    row2 = pick_beeper()
    while hubo.front_is_clear():
        hubo.move()
        row2 = 10 * row2 + pick_beeper()
    right_turn()

    carry = 0
    while hubo.front_is_clear() and (row2 != 0 or carry != 0):
        row1 = pick_beeper()
        tot = row1 + carry + (row2 % 10)
        row2 //= 10
        carry = tot // 10
        drop_beeper(tot % 10)
        hubo.move()

hubo.turn_left()
hubo.move()
turn_right()
while hubo.front_is_clear() and not hubo.on_beeper():
    hubo.move()
add()
