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

directions ={
    1: "E",
    2: "W",
    3: "S",
    4: "N"
}


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


def makeHuboMove():
    cnt = pick_beeper()
    if cnt == 0:
        drop_beeper(5)
    else:
        turn(directions[cnt])
        hubo.move()
        makeHuboMove()


def escape():
    ###################################
    # Implement here
    #####################################
    makeHuboMove()
    

#----------------------------------------
# Do not modify main()!!
#---------------------------
def main():
    if _world == None:
	    load_world('worlds/ex2.wld')
    global hubo
    hubo = Robot(avenue=1, street=1, beepers=10000)
    escape()
    
if __name__ == "__main__":
    main()
