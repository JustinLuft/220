"""
Justin Luft
vigenere.py

Problem: develop a vigenere cypher with a keyword

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""
from graphics import *
def code(s, h):
    s = s.upper()
    s = s.replace(" ", "")
    length = int(len(h)) - 1
    h = h.upper()
    acc = ""
    keyacc = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(s)):
        letterinh = h[keyacc]
        vinereh = alpha.find(str(letterinh))
        letterins = s[i]
        vinere_alpha = alpha.find(str(letterins))
        encodednum = vinereh + vinere_alpha
        if int(encodednum) > 25:
            encodednum = encodednum - 26
        encoded = alpha[int(encodednum)]
        acc = acc + encoded
        if keyacc < length:
            keyacc = keyacc + 1
        else:
            keyacc = 0

    return(acc)
def main():
    win = GraphWin("Vigenere", 500, 500)
    text1 = Text(Point(100, 100), "Message to code")
    text1.draw(win)
    text2 = Text(Point(100, 150), "Key")
    text2.draw(win)
    buttonoutline = Rectangle(Point(210, 200), Point(290, 250))
    buttonoutline.draw(win)
    text3 = Text(Point(250, 225), "Encode")
    text3.draw(win)
    enters = Entry(Point(260, 100), 25)
    enters.draw(win)
    enterh = Entry(Point(260, 150), 25)
    enterh.draw(win)
    win.getMouse()
    s = str(enters.getText())
    h = str(enterh.getText())
    s = s.upper()
    s = s.replace(" ", "")
    length = int(len(h)) - 1
    h = h.upper()
    acc = ""
    keyacc = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(s)):
        letterinh = h[keyacc]
        vinereh = alpha.find(str(letterinh))
        letterins = s[i]
        vinere_alpha = alpha.find(str(letterins))
        encodednum = vinereh + vinere_alpha
        if int(encodednum) > 25:
            encodednum = encodednum - 26
        encoded = alpha[int(encodednum)]
        acc = acc + encoded
        if keyacc < length:
            keyacc = keyacc + 1
        else:
            keyacc = 0
    buttonoutline.undraw()
    text3.undraw()
    text4 = Text(Point(250, 250), acc)
    text4.draw(win)
    text5 = Text(Point(250, 225), "Resulting Message")
    text5.draw(win)
    text6 = Text(Point(250, 400), "Click anywhere to close")
    text6.draw(win)
    win.getMouse()
    win.Close()
if __name__ == '__main__':
    main()