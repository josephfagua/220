"""
Name: Joseph Fagua
lab3.py
"""


def average():
    hw = eval(input("Enter the number of HW"))
    acc = 0
    for i in range(hw):
        grade = eval(input("Enter grade for HW" + str(i + 1)))
        acc = acc + grade
    average_grade = acc / hw
    print("Average Grade:", round(average_grade, 2))


def tip_jar():
    acc = 0
    for i in range(1, 5 + 1):
        donation = eval(input("Enter donation amount"))
        acc = acc + donation
    print("total: ", acc)


def newton():
    x = eval(input("Enter x"))
    refine = eval(input("Enter number of refinements"))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print("Final value:", approx)


def sequence():
    terms = eval(input("Enter the number of terms in series"))
    for i in range(terms):
        y = 1 + ((i+1)//2 * 2)
        print(y)


def pi():
    term = eval(input("Enter the number of terms in series"))
    acc = 1
    for i in range(term):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i +1)//2 * 2)
        frac = num / denom
        acc = acc * frac
    print(acc * 2)





