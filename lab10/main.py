import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1graphics import *
# from cs1graphics import *
from time import sleep

_scene = None
_world = None

def create_world():
    global _scene, _world
    if _scene:
        raise RuntimeError("A world already exists!")
    _world = _World(500, 300)
    _scene = Canvas(_world.width, _world.height)
    _scene.setTitle("Mario World")
    _world.draw_scene()

class _World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_scene(self):
        """
        draw background here
        Don't forget _scene.add(name)
        """
        pass


"""
define your own objects, e.g. Mario and Mushroom

class Mushroom (object):
    def __init__(self, x, y):
        mushroom = Layer()

        uppermush = Ellipse(38, 18, Point(x, y))
        uppermush.setFillColor('red')
        uppermush.setDepth(52)
        mushroom.add(lowermush)

        lowermush = Ellipse(35, 25, Point(x, y+8))
        lowermush.setFillColor('beige')
        lowermush.setDepth(53)
        mushroom.add(uppermush)

        mushroom.setDepth(52)

        self.layer = mushroom   # save mushroom shape in the class
        _scene.add(self.layer)  # add to global Canvas

class Mario (object):
    def __init__(self, ...
        self.layer = Layer()
        ...
        _scene.add(self.layer)
"""



create_world()
# define your objects, e.g. mario = Mario('blue', 'normal')

# write your animation scenario here

'''

Upgrade your wonderful animal. Refer to an example marioworld.py.

Tasks
Recall the animal you created.

But this time, make it much more elegant.
Use Python objects so that you can make it like hubo in cs1robots.
Requirements for your new animal object:

It should have parameters for the constructor.
e.g. Initial position, colors, size, options, etc.
mario = Mario('blue', 'normal')
It must have methods that can be used to move it on the canvas, and to move its body parts.
You must not use the graphical objects outside the object.
It must have at least one event method which can change the animal’s shape or do special actions.
e.g. becoming Super Mario, laying eggs, transforming, etc.

'''