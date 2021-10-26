"""
Justin Luft
weighted_average.py
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "wt")
    gradefinal = 0
    classavg = 0
    acc2 = 0
    for line in infile:
        acc1 = 0
        gradeacc = 0
        split1 = line.split(':')
        name = split1[0]
        split2 = split1[1]
        gradeval = split2.split()
        for num in gradeval[0::2]:
            acc1 = acc1 + int(num)
        if acc1 != 100:
            if acc1 > 100:
                output.write(str(name) + "'s average: " + "Error: The weights are more than 100" + "\n")
            else:
                output.write(str(name) + "'s average: " + "Error: The weights are less than 100" + "\n")
            acc2 = acc2 - 1
        else:
            for num in gradeval[0::2]:
                num2 = int(gradeval.index(num)) + 1
                theweight = int(num)
                thegrade = int(gradeval[num2])
                grade = thegrade * theweight
                gradeacc = gradeacc + grade
                gradefinal = gradeacc / 100
            output.write(str(name) + "'s average: " + str(gradefinal) + "\n")
            classavg = classavg + float(gradefinal)
        acc2 = acc2 + 1
    classavg1 = classavg / acc2
    output.write("Class Average: " + str(classavg1))








