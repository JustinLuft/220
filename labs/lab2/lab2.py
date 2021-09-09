"""
Name: Justin Luft
lab2.py

Problem: Develop simple Python programs that do input, produce output and do arithmetic.
"""
import math
def sum_of_threes():
    bound = eval(input("What is the upper bound?"))
    acc = 0
    for i in range(0, bound + 1, 3):
         acc = i + acc
    print(acc)
def multiplication_table():
    for a in range (1, 11):
        for b in range (1, 11):
            print(a *b, end=" ")
        print()
def triangle_area():
    a = eval(input("What is the length of side a?"))
    b = eval(input("What is the length of side b?"))
    c = eval(input("What is the length of side c?"))
    s = (a + b + c) / 2
    part1 = (s - a) * (s - b) * (s - c)
    part2 = part1 * s
    capA = math.sqrt(part2)
    print(capA)
def sumSquares():
    start = eval(input("What is the starting number?"))
    ending = eval(input("What is the ending number?"))
    acc1 = 0
    acc2 = 0
    for numb in range(start, ending + 1, 1):
        acc1 = numb ** 2
        acc2 = acc1 + acc2
    print(acc2)
def power():
    base = eval(input("What is the base number?"))
    exponent = eval(input("What is the exponent?"))
    acc = 1
    for anum in range (exponent):
        acc = acc * base
    print(acc)
