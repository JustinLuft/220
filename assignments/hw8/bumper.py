"""

"""
import math
from random import *
from graphics import *
from time import *
def hit_vertical(circle, window):
    circlex = circle.getP1()
    circlexreal = circlex.getX()
    circler = circle.getRadius()
    avoid = 500 - 2 * circler
    if circlexreal < avoid and circlexreal > 0:
        return True
    else:
        return False
def hit_horizontal(circle, window):
    circley = circle.getP1()
    circleyreal = circley.getY()
    circler = circle.getRadius()
    avoid = 500 - 2 * circler
    if circleyreal < avoid and circleyreal > 0:
        return True
    else:
        return False
def didCollide(circle1, circle2):
    p1 = circle1.getP1()
    p3 = circle2.getP1()
    radius = circle1.getRadius()
    radius2 = circle2.getRadius()
    distancecore = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    radiuscom = radius + radius2
    if distancecore <= radiuscom:
        return False
    else:
        return True



def main():
    win = GraphWin("Bumpers", 500, 500)
    point1 = 250
    point2 = 250
    point3 = 350
    point4 = 350
    circle1 = Circle(Point(point1, point2), 30)
    circle1.draw(win)
    circle1.setFill("blue")
    circle2 = Circle(Point(point1, point2), 30)
    circle2.draw(win)
    circle2.setFill("red")
    while 1 == 1:
        #circle 1
        print("redo")
        xory_1 = randint(-100, 100)
        xory1 = xory_1 / 100
        xory_2 = randint(-100, 100)
        xory2 = xory_2 / 100

        xory_3 = randint(-100, 100)
        xory3 = xory_3 / 100
        xory_4 = randint(-100, 100)
        xory4 = xory_4 / 100
        while hit_vertical(circle2, win) and hit_horizontal(circle2, win) and hit_vertical(circle1, win) and hit_horizontal(circle1, win) == True:
            circle2.move(xory3, 0)
            circle2.move(0, xory4)
            circle1.move(xory1, 0)
            circle1.move(0, xory2)
        while hit_vertical(circle2, win) and hit_vertical(circle1, win) == False:
            xoryneg = xory3 * -1
            circle2.move(xoryneg, 0)
            xoryneg = xory1 * -1
            circle1.move(xoryneg, 0)
        while hit_horizontal(circle1, win) and hit_horizontal(circle2, win) == False:
            xoryneg = xory2 * -1
            circle1.move(0, xoryneg)
            xoryneg = xory4 * -1
            circle2.move(0, xoryneg)

        while hit_vertical(circle2, win) and hit_horizontal(circle2, win) == True:
            circle2.move(xory3, 0)
            circle2.move(0, xory4)
        while hit_vertical(circle2, win) == False:
            xoryneg = xory3 * -1
            circle2.move(xoryneg, 0)
        while hit_horizontal(circle2, win) == False:
            xoryneg = xory4 * -1
            circle2.move(0, xoryneg)

        while hit_vertical(circle1, win) and hit_horizontal(circle1, win) == True:
            circle1.move(xory1, 0)
            circle1.move(0, xory2)
        while hit_vertical(circle1, win) == False:
            xoryneg = xory1 * -1
            circle1.move(xoryneg, 0)
        while hit_horizontal(circle1, win) == False:
            xoryneg = xory2 * -1
            circle1.move(0, xoryneg)
main()