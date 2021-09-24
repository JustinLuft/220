"""
Name: Justin Luft

Problem: Practice accumulations and nested loops

Certification of Authenticity
I certify that this assignment is entirely my own work.

"""
def main():
    roadssurveyed = eval(input("How many roads were surveyed?"))
    acc = 0
    avg = 0
    totalveh = 0
    for acc in range(roadssurveyed):
        miniacc = 0
        vehaccum = 0
        acc = acc + 1
        print("How many days was road", acc, end=(""))
        days = eval(input(" surveyed for?"))
        for miniacc in range(days):
            miniacc = miniacc + 1
            print("How many cars traveled on day", miniacc, end=(""))
            carstrav = eval(input("?"))
            vehaccum = vehaccum + carstrav
            avg = vehaccum / days
        totalveh = totalveh + vehaccum
        print("Road ", acc, " average vehicles per day: ", avg)
    averageper = totalveh / roadssurveyed
    print("Total number of vehicles traveled on all roads:", totalveh)
    print("Average number of vehicles per roads:", round(averageper, 2))

if __name__ == '__main__':
    main()
