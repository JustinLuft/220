"""
Button class
"""
from graphics import *
class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text
    def get_label(self):
        text = self.text
        text = text.getText()
        return text

    def draw(self, win):
        clickable = self.shape
        clickable.draw(win)
        self.clickable = clickable
        texty = self.text
        texty.draw(win)

    def undraw(self):
        shape = self.clickable
        text = self.textbox
        shape.undraw()
        text.undraw()

    def is_clicked(self, mouseclick):
        shape = self.shape
        rec1 = shape.getP1()
        p1x = rec1.getX()
        p1y = rec1.getY()
        rec2 = shape.getP2()
        p2x = rec2.getX()
        p2y = rec2.getY()
        mouseclickx = mouseclick.getX()
        mouseclicky = mouseclick.getY()
        if p1x >= p2x:
            if mouseclickx <= p1x and mouseclickx >= p2x:
                if p1y >= p2y:
                    if mouseclicky <= p1y and mouseclicky >= p2y:
                        return True
                elif p2y >= p1y:
                    if mouseclicky < p2y and mouseclicky > p1y:
                        return True
        elif p2x >= p1x:
            if mouseclickx <= p2x and mouseclickx >= p1x:
                if p2y >= p1y:
                    if mouseclicky <= p2y and mouseclicky >= p1y:
                        return True
                elif p1y >= p2y:
                    if mouseclicky <= p1y and mouseclicky >= p2y:
                        return True
        return False

    def color_button(self, color):
        clickable = self.shape
        clickable.setFill(str(color))

    def set_label(self, label):
        newtext = self.text
        newtext.setText(label)














