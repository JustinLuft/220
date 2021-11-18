"""
Button class
"""
from graphics import *
class Button:
    def __init__(self, shape, text):
        self.shape = shape
        rec1 = shape.getP1()
        self.p1x = rec1.getX()
        self.p1y = rec1.getY()
        rec2 = shape.getP2()
        self.p2x = rec2.getX()
        self.p2y = rec2.getY()
        self.text = text
    def get_label(self):
        text = str(self.text)
        return text
    def draw(self, win):
        clickable = self.shape
        clickable.draw(win)
        centerxbef = self.p1x + self.p2x
        centerx = centerxbef / 2
        centerybef = self.p1y + self.p2y
        centery = centerybef / 2
        textbox = Text(Point(centerx, centery), str(self.text))
        textbox.draw(win)
        self.textbox = textbox


    def undraw(self, button, text):
        button.undraw()
        text.undraw()

    def set_label(self, label):
        newtext = self.textbox
        newtext.setText(label)

    def color_button(self, color):
        clickable = self.shape
        clickable.setFill(str(color))

    def is_clicked(self, mouseclick):
        mouseclickx = mouseclick.getX()
        mouseclicky = mouseclick.getY()
        if self.p1x >= self.p2x:
            if mouseclickx <= self.p1x and mouseclickx >= self.p2x:
                if self.p1y >= self.p2y:
                    if mouseclicky <= self.p1y and mouseclicky >= self.p2y:
                        return True
                elif self.p2y >= self.p1y:
                    if mouseclicky < self.p2y and mouseclicky > self.p1y:
                        return True
        elif self.p2x >= self.p1x:
            if mouseclickx <= self.p2x and mouseclickx >= self.p1x:
                if self.p2y >= self.p1y:
                    if mouseclicky <= self.p2y and mouseclicky >= self.p1y:
                        return True
                elif self.p1y >= self.p2y:
                    if mouseclicky <= self.p1y and mouseclicky >= self.p2y:
                        return True
        return False










