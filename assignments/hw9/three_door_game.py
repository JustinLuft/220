"""
three_door_game.py
A three door random game
I certify that this code is entirely written by me
"""
from random import *
from button import *
from graphics import *
winner = randint(1, 3)
win = GraphWin("Three Door Game", 500, 500)
Box1 = Rectangle(Point(340, 275), Point(455, 350))
Box1 = Button(Box1, "Box 3")
Box1.draw(win)
Box2 = Rectangle(Point(200, 275), Point(315, 350))
Box2 = Button(Box2, "Box 2")
Box2.draw(win)
Box3 = Rectangle(Point(60, 275), Point(175, 350))
Box3 = Button(Box3, "Box 1")
Box3.draw(win)
guider = Text(Point(250, 50), "I have a secret door")
guider.draw(win)
rules = Text(Point(250, 450), "Click to choose my door")
rules.draw(win)
theguess = win.getMouse()
if winner == 3:
    if Box1.is_clicked(theguess):
        Box1.color_button("lime")
        guider.setText("You Win!")
        rules.setText("Click to close")
    elif Box2.is_clicked(theguess):
        Box2.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
    elif Box3.is_clicked(theguess):
        Box3.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
if winner == 2:
    if Box1.is_clicked(theguess):
        Box1.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
    elif Box2.is_clicked(theguess):
        Box2.color_button("lime")
        guider.setText("You Win!")
        rules.setText("Click to close")
    elif Box3.is_clicked(theguess):
        Box3.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
if winner == 1:
    if Box1.is_clicked(theguess):
        Box1.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
    elif Box2.is_clicked(theguess):
        Box2.color_button("red")
        guider.setText("You Lost!")
        rules.setText("Door " + str(winner) + " was my secret door!")
    elif Box3.is_clicked(theguess):
        Box3.color_button("lime")
        guider.setText("You Win!")
        rules.setText("Click to close")

win.getMouse()
win.close()