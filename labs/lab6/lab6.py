"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def name_reverse():
   x = input("What is the name?")
   x2 = x.split()
   print(x2[1], x2[0])
def company_name():
    x = input("What is the company domain?")
    x2 = x.split(".")
    print(x2[1])
def initials():
    n = eval(input("How many students?"))
    for n in range(n):
        first = input("What is the students first name?")
        last = input("What is the students last name?")
        print(first + "'s initials are:", first[0] + last[0])
def names():
    names = input("Please enter the names, seperated by commas")
    names = names.split(",")
    for name in names:
        parts = name.split()
        print(parts[0][0] + parts[1][0])
def thirds():
    n = eval(input("How many sentences?"))
    for i in range(n):
        s = input("What is the sentence?")
        for n in (s[2:-1:3]):
            print(n, end = "")
def word_average():
    x = input("What is the sentence?")
    acc = 0
    acc2 = 0
    x = x.split()
    for word in (x):
        acc2 = acc2 + 1
        acc = acc + len(word)
    average = acc / acc2
    print("The average is", average)
def pig_latin():
    x = input("What is the sentence?")
    x = x.lower()
    x = x.split()
    for word in (x):
        firstpart1 = word[-1]
        firstpart2 = word[1:-1]
        lastpart = word[0]
        print(firstpart2 + firstpart1 + lastpart + "ay", end = " ")
def main():
    # name_reverse()
    # company_name()
    # initials()
    # add other function calls here
    # names()
    # thirds()
    # word_average()
    pig_latin()

main()
