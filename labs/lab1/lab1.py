"""
Name: Justin Luft
lab1.py

Problem: This program has five different functions, one calculates the area of a triangle, one calculates the volume of a box,
one calculates shooting percentage, one calculates the total cost of a coffee purchase, and one translates kilometers to hours.
"""
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Etter the width:"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("The Volume is =", volume)
def shooting_percentage():
    shots = eval(input("What was the total amount of shots"))
    shotsmade = eval(input("How many shots were made?"))
    shotsdec = shotsmade / shots
    shotsperc = shotsdec * 100
    print("Your shooting percentage is", shotsperc, "%")
def coffee():
    coffeecost = 10.5
    shipcost = .86
    perpound = coffeecost + shipcost
    fixed = 1.5
    poundspurchased = eval(input("How many pounds of coffee are being purchased?"))
    coffeecost = poundspurchased * perpound
    total = coffeecost + fixed
    print("Your total cost of this purchase is $",total)
def kilometers_to_miles():
    kilotraveled = eval(input("How many kilometers were traveled?"))
    kilomile = 1.61
    milestraveled = kilotraveled / kilomile
    print("The amount of miles you traveled is", milestraveled)
