"""
Name: Justin Luft
lab8.py
"""
from encryption import encode, encode_better
def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "wt")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            output.write(str(i) + word + "\n")
            i = i + 1
def hourly_wages(in_file_name, out_file_name):
    wageraise = 1.65
    infile = open(in_file_name, "r")
    output = open(out_file_name, "wt")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + wageraise
        wage = wage * int(parts[3])
        output.write(str(parts[0]) + 's pay for this week is  ' + str(wage) + "\n")
def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + (pos * int(isbn[i]))
    return acc
def send_message(file, friend):
    infile = open(file, "r")
    output = open(friend, "wt")
    for line in infile:
        line = str(line)
        output.write(line)
def send_safe_message(file, friend, key):
    infile = open(file, "r")
    output = open(friend, "wt")
    for line in infile:
        line = encode(str(line), key)
        line = str(line)
        output.write(line)
def send_uncrackable_message(file, friend, Pad):
    padfile = open(Pad, "r")
    key = padfile.read()
    infile = open(file, "r")
    output = open(friend, "wt")
    for line in infile:
        line = encode_better(str(line), key)
        line = str(line)
        output.write(line + key)


