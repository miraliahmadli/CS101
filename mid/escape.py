import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *
import cs101_libraries_py35.cs1robots as cs1robots
#----------------------------------------
# Do not modify 
_world = cs1robots._world
hubo = None
#----------------------------------------


def fixWrongBeepers():
    #----------------------
    # Implement here
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

    reverse_directions ={
        1: "E",
        2: "W",
        3: "S",
        4: "N"
    }
    
    ans = 0
    while True:
        # if not hubo.on_beeper():
        #     hubo.turn_left()
        #     hubo.turn_left()
        #     break
        cnt = pick_beeper()
        l = 0
        if hubo.front_is_clear():
            direction = reverse_face_map[(face_map[face]) % 4]
        elif hubo.left_is_clear():
            l = 1
            direction = reverse_face_map[(face_map[face] + 1) % 4]
        elif hubo.right_is_clear():
            l = 2
            direction = reverse_face_map[(face_map[face] + 3) % 4]
        else:
            if cnt != 0:
                ans += 1
            break
        if cnt == 0 or direction != reverse_directions[cnt]:
            ans += 1
            cnt = directions[direction]
        drop_beeper(cnt)
        if l == 0:
            hubo.move()
        elif l == 1:
            hubo.turn_left()
            hubo.move()
        elif l == 2:
            turn_right()
            hubo.move()
        face = direction

    #---------------------
    return ans # modify this line to return the number of locations fixed
    
#----------------------------------------
# Do not modify main() but load_world()!!
#-----------------------------------------
def main():
    if _world == None:
	    load_world('worlds/maze4.wld') # you can modify this line to test another world.
    global hubo
    hubo = Robot(avenue=1, street=1, beepers=10000)
    print("Returned Value:", fixWrongBeepers())
    
if __name__ == "__main__":
    main()
