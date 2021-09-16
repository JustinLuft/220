"""
Name: Justin Luft
lab3.py
"""
def average():
    numgrades = eval(input("How many homework grades do you have to input?"))
    acc1 = 0
    allgrade = 0
    for i in range(numgrades):
        acc1 = acc1 + 1
        print("---Homework grade #", acc1)
        thegrade = eval(input("Please enter the homework grade"))
        allgrade = allgrade + thegrade
    avg = allgrade / numgrades
    print("Your average homework grade is", avg)
def tip_jar():
    acc1 = 0
    allmoney = 0
    for i in range(5):
        acc1 = acc1 + 1
        print("Hello person #", acc1)
        money = eval(input("How much money would you like to donate?"))
        allmoney = money + allmoney
    print("The total amount of money donated is $", allmoney)
def newton():
    x = eval(input("What is the number, x?"))
    numapprox = eval(input("How many times would you like to improve the approximation?"))
    approx = x / 2
    for i in range(numapprox):
        step1 = x / approx
        step2 = approx + step1
        approx = step2 / 2
    print("The final value of the approximation is,", approx)
def sequence():
    numseq = eval(input("How many numbers of terms in the series do you want?"))
    acc = 1
    print(1, end=(" "))
    for i in range(numseq):
        acc = 2 + acc
        print(acc, acc, end=(" "))
def pi():
    terms = eval(input("How many terms of pi would you like?"))
    acc = 1
    for i in range(terms):
        numer = 2 + (i//2 * 2)
        denomer = 1 + ((i+1)//2 * 2)
        frac = numer / denomer
        acc = acc * frac
    print(acc * 2)
