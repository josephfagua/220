"""
Name: Joseph Fagua
weighted_average.py

Purpose: create a program that takes an input doc and outputs an average

Certification of Authenticity:
I certify that this work is entirely my own.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    students = 0
    class_avg = 0
    for line in infile:
        parts = line.split(': ')
        name = parts[0]
        fl = name + "'s"
        sv = parts[1]
        student_values = sv.split()
        wn = student_values[0::2]
        gn = student_values[1::2]
        acc = 0
        gng = 0
        for i in wn:
            weighted = int(i)
            acc = acc + weighted
        if acc < 100:
            outfile.write(fl + " Error:" + " The weights are less than 100." + '\n')
        elif acc > 100:
            outfile.write(fl + " Error:" + " The weights are more than 100." + '\n')
        else:
            students += 1
            for i in range(len(gn)):
                grade = int(gn[i])
                weight = int(wn[i])
                grade = grade * weight
                gng = gng + grade
            gng = round(gng / 100, 1)
            class_avg = class_avg + gng
            outfile.write(fl + " average" + ':' + '\n')
    # average class here
    # round class avg to 1 decimal as well
    # divide the total class grade by students

def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
