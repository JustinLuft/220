"""
Name: Justin Luft

Problem: Calculate the mean
1) My program will calculate the mean of a given set of numbers
2) The inputs will be the amount of numbers, and the numbers. The output will be the mean.
3) The program will ask for the amount of numbers, the ask for the numbers, then print their mean.

Certification of Authenticity
I certify that this assignment is entirely my own work.

"""
import math
def main():
    amount = eval(input("How many numbers are there?"))
    total = 0
    geototal = 1
    harmtotal = 0
    rmsnum = 0
    for num in range(amount):
        num = eval(input("What is the number?"))
        total = total + num
        squared = (num) ** 2
        rmsnum = squared + rmsnum
        geototal = geototal * num
        num3 = 1 / num
        harmtotal = num3 + harmtotal
    mean = total / amount
    rms1 = rmsnum / amount
    rms_average = math.sqrt(rms1)
    harmonic_mean = amount / harmtotal
    top = 1 / amount
    geometric_mean = geototal ** top
    print(mean)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))
    if __name__ == '__main__':
        main()
