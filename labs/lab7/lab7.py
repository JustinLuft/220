"""
Name: Justin Luft

lab7.py
"""
import math
def cash_conversion():
    x = eval(input("What is the integer?"))
    print('{:.2f}'.format(x))

def encode():
    s = input("What  you want encoded?")
    h = eval(input("What is the key value?"))
    acc = ""
    for c in s:
        i = ord(c) + h
        c = chr(i)
        acc = acc + c
    print(acc)

def sa(radius):
     area = 4 * 3.14 * radius ** 2
     return area

def sv(radius):
    volume = (4 / 3) * 3.14 * radius ** 3
    return volume

def sum_n(n):
    acc1 = 0
    for i in range(n):
        acc1 = i + acc1
    return acc1

def sum_n_cubes(n):
    acc2 = 0
    for i in range(n):
        cubed = i ** (1./3)
        acc2 =  acc2 + cubed
    return acc2
def encode_better():
    s = input("What  you want encoded?")
    h = input("What is the key")
    acc = ""
    for i in range(len(s)):
        c = s[i]
        key = h[i%len(h)]
        key = ord(key)-97
        i = ord(c) + key
        c = chr(i)
        acc = acc + c
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sa(3))
    print(sv(3))
    print(sum_n(5))
    print(sum_n_cubes(5))
    encode_better()
    pass


main()
