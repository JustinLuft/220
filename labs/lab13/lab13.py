"""
Justin Luft
Lab13.py
"""
from graphics import *

def iib(search, values):
    mid = len(values)//2
    print(mid)
    while search != values[mid] and len(values) != 1:
        if search < values[mid]:
            values = values[:mid]
            print(values[mid:])
        else:
            values = values[mid:]
            print(values[:mid])
        mid = len(values) // 2
    if values[mid] == search:
        return True
    return False
def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        print(lowest)
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]

def rec_sort(values):
    d = {}
    areas = []
    for rect in values:
        d[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]

def calc_area(rect):
    p1 = rect.getP1()
    p1x = p1.getX()
    p1y = p1.getY()
    p2 = rect.getP2()
    p2x = p2.getX()
    p2y = p2.getY()
    if p1x >= p2x:
        height = p1x - p2x
    else:
        height = p2x - p1x
    if p1y >= p2y:
        base = p1y - p2y
    else:
        base = p2y - p1y
    area = base * height
    return area

def trade_alert(filename):
    acc = 0
    infile = open(filename, "r")
    for line in infile:
        sales = line.split(" ")
    for i in sales:
        acc = acc + 1
        if int(i) > 830:
            print("Seconds:" + str(acc) + " Warning: trade volume exceded 830")
        elif int(i) > 500:
            print("Seconds:" + str(acc) + " Pay Attention!")

