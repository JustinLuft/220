"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
import math

from graphics import *
def addTens(nums):
    ten2 = 0
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * 2
def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        number = nums[i]
        sum = number + sum
    return sum
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
def writeSumOfSquares(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        nums = sumList(nums)
        output.write('Sum: ' + str(nums) + "\n")
def starter(weight, numWins):
    no = "You may not start"
    if numWins >= 5:
        if weight < 200:
            if weight >= 150:
                if weight <= 160:
                    print("You may start")
                else:
                    print(no)
            else:
                print(no)
        else:
            if numWins > 20:
                print("You may start")
            else:
                print(no)
    else:
        print(no)
def leapYear(year):
    yeardev4 = year % 4
    yeardev400 = year % 400
    yeardev100 = year % 100
    if yeardev4 == 0:
        if yeardev400 == 0:
            return(True)
        elif yeardev100 == 0:
            return(False)
        else:
            return (False)
    else:
        return (False)
def circleOverlap():
    win = GraphWin("CircleOverlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)
    distancecore = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    radiuscom = radius + radius2
    if distancecore <= radiuscom:
        test = Text(Point(250, 50), "The circles overlap")
        test.draw(win)
    else:
        test = Text(Point(250, 50), "The circles do not overlap")
        test.draw(win)



    win.getMouse()
    win.close()



