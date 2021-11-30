"""
Justin Luft
Greeting.py

Problem: Valentine's Day Card

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""
from time import sleep
from graphics import GraphWin, Text, Point, Polygon, Circle, Rectangle

def main():
    win = GraphWin("Valentines Day Greeting", 500, 500)
    win.setBackground("pink")
    sleep(2)
    greeting_txt = Text(Point(250, 50), "Happy Valentines Day!")
    greeting_txt.setSize(20)
    greeting_txt.setTextColor("Yellow")
    greeting_txt.setStyle("bold")
    greeting_txt.draw(win)
    acc = 0
    trip1 = 350
    trip2 = 411
    recp3 = 410
    recp4 = 490
    shape = Polygon(Point(250.0, 350.0), Point(146.0, 195.0), Point(350.0, 195.0))
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)
    shape2 = Circle(Point(200, 159), 65)
    shape2.setFill("red")
    shape2.setOutline("red")
    shape2.draw(win)
    shape3 = Circle(Point(295, 159), 65)
    shape3.setFill("red")
    shape3.setOutline("red")
    shape3.draw(win)
    sleep(3)
    for acc in range(15):
        acc =  acc + 1
        trip1 = trip1 - acc
        trip2 = trip2 - acc
        recp3 = recp3 - acc
        recp4 = recp4 - acc
        shape4 = Rectangle(Point(recp3, 225.0), Point(recp4, 255.0))
        shape4.setFill("gold")
        shape4.setOutline("gold")
        shape5 = Polygon(Point(trip1, 241.0), Point(trip2, 211.0), Point(trip2, 268.0))
        shape5.setFill("gold")
        shape5.setOutline("gold")
        shape4.draw(win)
        shape5.draw(win)
        sleep(0.5)
        shape5.undraw()
        shape4.undraw()
    shape5 = Polygon(Point(trip1, 241.0), Point(trip2, 211.0), Point(trip2, 268.0))
    shape5.setFill("gold")
    shape5.setOutline("gold")
    shape5.draw(win)
    shape4 = Rectangle(Point(recp3, 225.0), Point(recp4, 255.0))
    shape4.setFill("gold")
    shape4.setOutline("gold")
    shape4.draw(win)
    win.getMouse()
    win.close()
main()
