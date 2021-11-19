"""
Button class
"""
from graphics import *
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label
        rec1 = shape.getP1()
        p1x = rec1.getX()
        p1y = rec1.getY()
        rec2 = shape.getP2()
        p2x = rec2.getX()
        p2y = rec2.getY()
        centerxbef = p1x + p2x
        centerx = centerxbef / 2
        centerybef = p1y + p2y
        centery = centerybef / 2
        text = Text(Point(centerx, centery), self.text)
        self.text = text

    def get_label(self):
        text = self.text
        text = text.getText()
        return text

    def draw(self, win):
        clickable = self.shape
        clickable.draw(win)
        textbox = self.text
        textbox.draw(win)

    def undraw(self):
        shape = self.shape
        text = self.text
        shape.undraw()
        text.undraw()

    def set_label(self, label):
        newtext = self.text
        newtext.setText(label)

    def color_button(self, color):
        clickable = self.shape
        clickable.setFill(str(color))

    def is_clicked(self, mouseclick):
        mouseclickx = mouseclick.getX()
        mouseclicky = mouseclick.getY()
        shape = self.shape
        rec1 = shape.getP1()
        p1x = rec1.getX()
        p1y = rec1.getY()
        rec2 = shape.getP2()
        p2x = rec2.getX()
        p2y = rec2.getY()
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