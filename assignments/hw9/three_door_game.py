"""
three_door_game.py
A three door random game
I certify that this code is entirely written by me
"""
from random import *
from button import *
from graphics import *
def main():
    winner = randint(1, 3)
    win = GraphWin("Three Door Game", 500, 500)
    box1 = Rectangle(Point(340, 275), Point(455, 350))
    box1 = Button(box1, "Box 3")
    box1.draw(win)
    box2 = Rectangle(Point(200, 275), Point(315, 350))
    box2 = Button(box2, "Box 2")
    box2.draw(win)
    box3 = Rectangle(Point(60, 275), Point(175, 350))
    box3 = Button(box3, "Box 1")
    box3.draw(win)
    guider = Text(Point(250, 50), "I have a secret door")
    guider.draw(win)
    rules = Text(Point(250, 450), "Click to choose my door")
    rules.draw(win)
    theguess = win.getMouse()
    if winner == 3:
        if box1.is_clicked(theguess):
            box1.color_button("lime")
            guider.setText("You Win!")
            rules.setText("Click to close")
        elif box2.is_clicked(theguess):
            box2.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
        elif box3.is_clicked(theguess):
            box3.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
    if winner == 2:
        if box1.is_clicked(theguess):
            box1.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
        elif box2.is_clicked(theguess):
            box2.color_button("lime")
            guider.setText("You Win!")
            rules.setText("Click to close")
        elif box3.is_clicked(theguess):
            box3.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
    if winner == 1:
        if box1.is_clicked(theguess):
            box1.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
        elif box2.is_clicked(theguess):
            box2.color_button("red")
            guider.setText("You Lost!")
            rules.setText("Door " + str(winner) + " was my secret door!")
        elif box3.is_clicked(theguess):
            box3.color_button("lime")
            guider.setText("You Win!")
            rules.setText("Click to close")

    win.getMouse()
    win.close()
if __name__ == '__main__':
    main()