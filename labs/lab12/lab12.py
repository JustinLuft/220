"""
Justin Luft
lab12.py
"""
from random import *
def find_and_remove(list, value):
    try:
        spot = list.index(value)
        list[spot] = "Justin"
    except:
        pass

def read_data(file):
    file = open(file, "r")
    data = file.read()
    data = data.split()
    i = 0
    while i <= len(data):
        data[i] = int(data[i])
        i += 1
    return data
def is_in_linear(value, values):
    i = 0
    while i < len(values):
        if values[i] == value:
            return True
        i += 1
    return False
def good_input():
    ninput = -1
    while ninput > 10 or ninput <1:
        ninput = eval(input("Please enter an input between 1 and 10."))
    return ninput
def num_digits():
    while True:
        num = eval(input("Enter a number, 0 or neg to end"))
        if num > 0:
            acc = 0
            while num != 0:
                num = num // 10
                acc = acc + 1
            print("num of divisions:" + str(acc))
        else:
            return False
def hi_low_game():
    winum = randint(1, 100)
    win = 0
    lives = 7
    while win == 0:
        if lives == 0:
            print("You lost! the number was: " + str(winum))
            return False
        guess = eval(input("Guess a number! Lives left: " + str(lives)))
        if guess == winum:
            win = 1
            print("Winner!")
            return True
        else:
            lives = lives - 1






