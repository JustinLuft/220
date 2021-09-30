"""
Name: Justin Luft
lab5.py
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    r = 50
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    shape = Circle(Point(250, 250), r * 5)
    shape.setFill("white")
    shape.draw(win)
    shape = Circle(Point(250, 250), r * 4)
    shape.setFill("black")
    shape.draw(win)
    shape = Circle(Point(250, 250), r * 3)
    shape.setFill("blue")
    shape.draw(win)
    shape = Circle(Point(250, 250), r * 2)
    shape.setFill("red")
    shape.draw(win)
    shape = Circle(Point(250, 250), r)
    shape.setFill("yellow")
    shape.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    shape = Polygon(p1, p2, p3)
    shape.setFill("blue")
    shape.draw(win)
    dx1 = p2.getX() - p1.getX()
    dy1 = p2.getY() - p1.getY()
    abef = dx1 ** 2 + dy1 ** 2
    a = math.sqrt(abef)
    #side2
    dx2 = p3.getX() - p2.getX()
    dy2 = p3.getY() - p2.getY()
    bbef = dx2 ** 2 + dy2 ** 2
    b = math.sqrt(bbef)
    #side3
    dx3 = p3.getX() - p1.getX()
    dy3 = p3.getY() - p1.getY()
    cbef = dx3 ** 2 + dy3 ** 2
    c = math.sqrt(cbef)
    sbef = a + b + c
    s = sbef / 2
    sa = s - a
    sb = s - b
    sc = s - c
    smulti = s * sa * sb * sc
    area = math.sqrt(smulti)
    perimeter = a + b + c
    area_txt = Text(Point(230, 20), "The area is " + str(area) + " The perimeter is " + str(perimeter))
    area_txt.draw(win)
    # and display its area in the graphics window.
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")


    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        # entry1
        user_input1 = Entry(Point(210, 240), 10)
        user_input1.draw(win)
        # entry2
        user_input2 = Entry(Point(210, 270), 10)
        user_input2.draw(win)
        # entry3
        user_input3 = Entry(Point(210, 300), 10)
        user_input3.draw(win)
        win.getMouse()
        red = int(user_input1.getText())
        green = int(user_input2.getText())
        blue = int(user_input3.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
    # display rgb text
    # Wait for another click to exit
    win.getMouse()
    win.close()
def process_string():
    s = input("What is the string?")
    acc = 0
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    for i in range(10):
        print(s[0:4])
    for i in range(len(s)):
        print(s[acc])
        acc = acc + 1
    print(len(s))
def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1] + values[3])
    print(float(values[0]) + float(values[2]))
    print(values[1] * 5)
    print(values[2], values [3], pt)
    print(values[2], values[3], values[1])
    print(values[2], values[3], float(values[-1]))
    print(float(values[0]) + float(values[2]) + float(values[-1]))
    print(len(values))
def another_series():
    acc = 0
    total = 0
    numterm = eval(input("How many terms?"))
    for i in range(numterm):
        num = 0
        if acc == 0:
            num = 2
        if acc == 1:
            num = 4
        if acc == 2:
            num = 6
        total = total + num
        acc = acc + 1
        if acc > 2:
            acc = 0
        print(num, end= " ")
    print(total)


def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()

    pass


main()
