"""
Name: Justin Luft

Problem: Compute the monthly interest charge on a credit card account

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""
def main():

 #user inputs
    annualir = eval(input("What is your credit card's annual interest rate? (percentage wise)"))
    bcycle = eval(input("What is the number of days in your billing Cycle?"))
    pnetbal = eval(input("What was the previous net balance?"))
    payment = eval(input("What is the payment amount?"))
    numpayment = eval(input("What was the day of the billing cycle in which the payment was made?"))
 #calculations
    step1 = pnetbal * bcycle
    days = bcycle - numpayment
    step2 = payment * days
    step3 = step1 - step2
    step4 = step3 / bcycle
    monthlyir = (annualir / 12) / 100
    mic = step4 * monthlyir
    mic = round(mic, 2)
    print(mic)

if __name__ == '__main__':
    main()
