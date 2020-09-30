import sys
sys.path.append("/Users/mirali/dev/CS101")

from cs101_libraries_py35.cs1graphics import *
from time import sleep


paper = Canvas()
paper.setBackgroundColor('midnight blue')
paper.setWidth(700)
paper.setHeight(450)
paper.setTitle("Sky")

planet1= Circle(220, Point(60,100))
planet1.setFillColor("orange")
planet1.setDepth(10)
planet1.setBorderColor("red")
planet1.setBorderWidth(10)
paper.add(planet1)

planet2= Circle(65, Point(570,300))
planet2.setFillColor("dark red")
planet2.setDepth(100)
paper.add(planet2)

rocket= Layer()
flame = Ellipse(50,12, Point(700,300))
flame2 = Ellipse(70,25, Point(715,300))
flame3 = Ellipse(90,25, Point(722,300))


def draw_animal():
    global rocket

    body=Rectangle(150,30, Point(600,300))
    body.setFillColor("gray")
    body.setDepth(50)
    rocket.add(body)

    top = Polygon(Point(525,280) , Point(525,320) , Point(500,300))
    top.setFillColor('red')
    top.setDepth(50)
    rocket.add(top)

    wing1 = Polygon(Point(620,285), Point(680,285), Point(680,265))
    wing1.setFillColor('red')
    wing1.setDepth(50)
    rocket.add(wing1)

    wing2 = Polygon(Point(620,315), Point(680,315), Point(680,335))
    wing2.setFillColor('red')
    wing2.setDepth(50)
    rocket.add(wing2)

    paper.add(rocket)

    global flame
    flame.setFillColor("orange")
    flame.setDepth(40)
    rocket.add(flame)

    global flame2
    flame2.setFillColor("yellow")
    flame2.setDepth(50)
    rocket.add(flame2)

    global flame3
    flame3.setFillColor("red")
    flame3.setDepth(70)
    rocket.add(flame3)


def show_animation():
    for i in range(50):
        rocket.move(-1,0)
        flame.scale(0.925)
        flame2.scale(0.925)
        flame3.scale(0.930)
    sleep(3)
    for i in range(50):
        rocket.move(-1,0)
        for i in range(1):
            flame.scale(1.07)
            flame2.scale(1.07)
            flame3.scale(1.07)

    for i in range(50):
        rocket.move(-1,0)
        for i in range(1):
            flame.scale(1.01)
            flame2.scale(1.01)
            flame3.scale(1.006)

    for i in range(80):
        rocket.move(-1,0)
        planet2.move(1,0)

    for j in range(300):
        planet2.move(1,0)
        planet1.scale(1.001)
        rocket.move(-1,0)

    
draw_animal()
show_animation()
