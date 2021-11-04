"""
Justin Luft
bumper.py
I certify that this assignment is entirely my own work.
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
def did_collide(circle1, circle2):
    p1 = circle1.getP1()
    p3 = circle2.getP1()
    radius = circle1.getRadius()
    radius2 = circle2.getRadius()
    distancecore = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    radiuscom = radius + radius2
    if distancecore <= radiuscom:
        return True
    else:
        return False
def get_random(int, move_amount):
    move_amount_neg = move_amount * -1
    int = randint(move_amount_neg, move_amount)
    return int
def main():
    random1 = randint(0, 255)
    random2 = randint(0, 255)
    random3 = randint(0, 255)
    red = int(random1)
    green = int(random2)
    blue = int(random3)
    color = color_rgb(red, green, blue)
    win = GraphWin("Bumpers", 500, 500)
    win.setBackground(color)

    point1 = randint(0, 470)
    point2 = randint(0, 470)
    point3 = randint(0, 470)
    point4 = randint(0, 470)
    radius1 = 30
    circle1 = Circle(Point(point1, point2), radius1)
    circle1.draw(win)
    random1 = randint(0, 255)
    random2 = randint(0, 255)
    random3 = randint(0, 255)
    red = int(random1)
    green = int(random2)
    blue = int(random3)
    color = color_rgb(red, green, blue)
    circle1.setFill(color)

    radius2 = 30
    circle2 = Circle(Point(point3, point4), radius2)
    circle2.draw(win)
    random1 = randint(0, 255)
    random2 = randint(0, 255)
    random3 = randint(0, 255)
    red = int(random1)
    green = int(random2)
    blue = int(random3)
    color = color_rgb(red, green, blue)
    circle2.setFill(color)
    xory1 = 0
    xory2 = 0
    xory3 = 0
    xory4 = 0
    while 1 == 1:
        #circle 1
        move_amount = randint(0, 10)
        xory1 = get_random(xory1, move_amount)
        xory2 = get_random(xory2, move_amount)

        xory3 = get_random(xory3, move_amount)
        xory4 = get_random(xory4, move_amount)
        while True:
            if did_collide(circle1, circle2) == True:
                xory1 = xory1 * -1
                xory2 = xory2 * -1
                xory3 = xory3 * -1
                xory4 = xory4 * -1
            if hit_vertical(circle1, win) == False:
                xory1 = xory1 * -1
            if hit_horizontal(circle1, win) == False:
                xory2 = xory2 * -1
            if hit_vertical(circle2, win) == False:
                xory3 = xory3 * -1
            if hit_horizontal(circle2, win) == False:
                xory4 = xory4 * -1
            circle1.move(xory1, 0)
            circle1.move(0, xory2)
            circle2.move(xory3, 0)
            circle2.move(0, xory4)
            circle2.move(xory3, 0)
            circle2.move(0, xory4)
            circle1.move(xory1, 0)
            circle1.move(0, xory2)
if __name__ == '__main__':
    main()
