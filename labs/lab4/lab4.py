"""
Justin Luft
lab4.py
"""
import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to Close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Rectangle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p1, p2)
    shape.setFill("red")
    shape.draw(win)
    length = abs(p1.getY() - p2.getY())
    width = abs(p1.getX() - p2.getX())
    area = length * width
    perimeter2 = length + width
    perimeter = perimeter2 * 2
    area_txt = Text(Point(120, 20), "The area is " + str(area) + " The perimeter is " + str(perimeter))
    area_txt.draw(win)
    ## Closing
    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "Click to close")
    instructions.draw(win)
    ##
    win.getMouse()
    win.close()
    pass
def circle():
    win = GraphWin("Circle", 400, 400)
    center = win.getMouse()
    p1 = win.getMouse()
    rad1 = center.getX() - p1.getX()
    rad2 = rad1 ** 2
    rad3 = center.getY() - p1.getY()
    rad4 = rad3 ** 2
    rad5 = rad2 + rad4
    rad6 = math.sqrt(rad5)
    shape = Circle(center, rad6)
    shape.setOutline("blue")
    shape.setFill("red")
    shape.draw(win)
    area_txt = Text(Point(120, 30),"The radius of the circle is " + str(rad6))
    area_txt.draw(win)
    ## Closing
    inst_pt = Point(200, 390)
    instructions = Text(inst_pt, "Click to close")
    instructions.draw(win)
    ##
    win.getMouse()
    win.close()
def pi2():
    terms = eval(input("How many terms would you like?"))
    answ = 0
    for bottom in range(terms):
        if bottom % 2 == 1:
            symb = -1
        else:
            symb = 1
        if bottom == 0:
            bottom = 1
        else:
            bottom = 2 * bottom + 1
        frac1 = 4 / bottom
        frac2 = frac1 * symb
        answ = answ + frac2
    print(answ)

def main():
    squares()
    rectangle()
    circle()
    pi2()

main()
