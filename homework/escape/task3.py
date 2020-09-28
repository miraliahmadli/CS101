import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
import cs101_libraries_py35.cs1robots as cs1robots

_world = cs1robots._world
hubo = None


face = "E"
face_map = {
    "E": 0,
    "N": 1,
    "W": 2,
    "S": 3
}

reverse_face_map = {
    0: "E",
    1: "N",
    2: "W",
    3: "S"
}

directions ={
    "E": 1,
    "W": 2,
    "S": 3,
    "N": 4
}


def turn_right():
    for _ in range(3):
        hubo.turn_left()


def pick_beeper():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
    return cnt


def drop_beeper(n):
    for _ in range(n):
        hubo.drop_beeper()


def turn(direction="E"):
    global face
    for _ in range((4 + face_map[direction] - face_map[face]) % 4):
        hubo.turn_left()
    face = direction


def get_direction():
    global face
    if hubo.left_is_clear():
        turns = 1
    elif hubo.right_is_clear():
        turns = 3
    else:
        turns = 2
    new_face = reverse_face_map[(face_map[face] + turns) % 4]
    turn(new_face)


def makePath():
    ###################################
    # Implement here
    #####################################
    global face
    path = []
    while not hubo.on_beeper():
        while hubo.front_is_clear():
            path.append(face)
            hubo.move()
        get_direction()
    
    hubo.pick_beeper()
    hubo.move()

    while len(path) != 0:
        direction = path.pop()
        drop_beeper(directions[direction])
        if hubo.front_is_clear():
            hubo.move()
        elif hubo.left_is_clear():
            hubo.turn_left()
            hubo.move()
        elif hubo.right_is_clear():
            turn_right()
            hubo.move()
        else:
            break

    
#----------------------------------------
# Do not modify main()!!
#---------------------------
def main():
    if _world == None:
	    load_world('worlds/maze.wld')
    global hubo
    hubo = Robot(avenue=1, street=1, beepers=10000)
    makePath()
    
if __name__ == "__main__":
    main()
