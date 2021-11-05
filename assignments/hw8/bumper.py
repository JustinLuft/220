"""
Justin Luft
bumper.py
I certify that this assignment is entirely my own work.
"""
import math
from random import randint
from graphics import Circle, color_rgb, Point, GraphWin

def hit_vertical(circle, win):
    winy = win.getWidth()
    circlex = circle.getP1()
    circlexreal = circlex.getX()
    circler = circle.getRadius()
    avoid = winy - 2 * circler
    return not(circlexreal < avoid and circlexreal > 0)

def hit_horizontal(circle, win):
    winx = win.getHeight()
    circley = circle.getP1()
    circleyreal = circley.getY()
    circler = circle.getRadius()
    avoid = int(winx) - 2 * circler
    return not(circleyreal < avoid and circleyreal > 0)

def did_collide(circle1, circle2):
    p_1 = circle1.getP1()
    p_3 = circle2.getP1()
    radius = circle1.getRadius()
    radius2 = circle2.getRadius()
    distancecore = math.sqrt((p_1.getX() - p_3.getX()) ** 2 + (p_1.getY() - p_3.getY()) ** 2)
    radiuscom = radius + radius2
    return distancecore <= radiuscom

def get_random(move_amount):
    move_amount_neg = move_amount * -1
    moveme = randint(move_amount_neg, move_amount)
    return moveme
def main():
    random1 = randint(0, 255)
    random2 = randint(0, 255)
    random3 = randint(0, 255)
    red = int(random1)
    green = int(random2)
    blue = int(random3)
    color = color_rgb(red, green, blue)
    win = GraphWin("Bumpers", 600, 400)
    win.setBackground(color)

    point1 = randint(0, 370)
    point2 = randint(0, 370)
    point3 = randint(0, 370)
    point4 = randint(0, 370)
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
    while True:
        #circle 1
        move_amount = randint(0, 20)
        xory1 = get_random(move_amount)
        xory2 = get_random(move_amount)

        xory3 = get_random(move_amount)
        xory4 = get_random(move_amount)
        while True:
            if did_collide(circle1, circle2):
                xory1 = xory1 * -1
                xory2 = xory2 * -1
                xory3 = xory3 * -1
                xory4 = xory4 * -1
            if hit_vertical(circle1, win):
                xory1 = xory1 * -1
            if hit_horizontal(circle1, win):
                xory2 = xory2 * -1
            if hit_vertical(circle2, win):
                xory3 = xory3 * -1
            if hit_horizontal(circle2, win):
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
