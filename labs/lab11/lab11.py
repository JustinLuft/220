"""
Justin Luft
lab11.py
"""
import random
def wordlist(in_file_name):
    infile = open(in_file_name, "r")
    acc = -1
    for line in infile:
        words = line.split()
    return words
def randomword(words):
    theword = random.choice(words)
    return theword
def wordcutter(theword):
    listlet = list(str(theword))
    return listlet
def guesser(listlet, badacc):
    allguessed = []
    acc = -1
    blanklist = []
    for i in range(len(listlet)):
        blanklist.append('_')
    while not(gameover(blanklist)):
        print(blanklist)
        print("Amount of lives left: " + str(badacc))
        theguess = eval(input('guess a letter!'))
        badacc = checker(theguess, blanklist, listlet, badacc, allguessed)
        if badacc == 0:
            print('You lost')
            break
def checker(theguess, blanklist, listlet, badacc, allguessed):
    acc = -1
    if theguess in listlet:
        for letter in listlet:
            acc = acc + 1
            if str(theguess) == str(letter):
                blanklist[acc] = theguess
    else:
        if str(theguess) not in allguessed:
            badacc = badacc - 1
            allguessed.append(theguess)
    print('Wrong letters: ' + str(allguessed))
    return badacc
def gameover(blanklist):
    acc = 0
    numb = 0
    for i in range(len(blanklist)):
        if blanklist[numb] != "_":
            acc = acc + 1
        numb = numb + 1
    if acc == int(len(blanklist)):
        print('You won!')
        return True
def game():
    badacc = 7
    listlet = wordcutter(randomword(wordlist('wordlist.txt')))
    guesser(listlet, badacc)
game()

