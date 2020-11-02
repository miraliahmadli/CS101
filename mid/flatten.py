import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1robots import *


def main():
    world = "./worlds/harvest1.wld"
    # world = "example/ex2.wld
    # load_world(world)
    create_world(avenues=12, streets=10)
    
    global hubo
    hubo = Robot(beepers = 500)
    hubo.set_trace("blue")
    flatten()
	
	

def flatten():
    ######ALL of your code must be here#########
    # Use the "hubo" variable defined in main()
    #
    # def your_function(): #define functions like this if you need
    #   ....
    def pick_beeper():
        while hubo.on_beeper():
            hubo.pick_beeper()
    
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
            pick_beeper()
            hubo.move()
        pick_beeper()
        if is_right_turn:
            succ = right_turn()
        else:
            succ = left_turn()
        if succ:
            return zigzag(not is_right_turn)
        return is_right_turn
    
    def zigzag2(is_right_turn=True):
        while hubo.front_is_clear():
            hubo.drop_beeper()
            hubo.move()
        hubo.drop_beeper()
        if is_right_turn:
            succ = right_turn()
        else:
            succ = left_turn()
        if succ:
            zigzag2(not is_right_turn)
    
    hubo.turn_left()
    is_right = zigzag()
    if is_right:
        turn_right()
    else:
        hubo.turn_left()
    zigzag2(is_right)
    while hubo.carries_beepers():
        hubo.drop_beeper()
    # Don't forget to submit your code through the "submit" button!
    ############################################

if __name__ == "__main__":
    main()
