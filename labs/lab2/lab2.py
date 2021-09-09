"""
Name: Joseph Fagua
lab2.py
"""


import math

def sum_of_threes():
    bound = eval(input("Enter upper bound:"))
    acc = 0
    for i in range (0, bound, 3):
        acc = i + acc
    print(acc)


def multiplication_table():
    for H in range (1,11):
        for L in range (1,11):
            print(H * L, end=" ")
        print( )


def triangle_area():
    a = eval(input("Enter Side 1:"))
    b = eval(input("Enter Side 2:"))
    c = eval(input("Enter Side 3:"))
    s = (a + b + c)/ 2
    A = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(A)
    print(area)

def sumSquares():
    lower_bound = eval(input("Enter the Lower Bound:"))
    upper_bound = eval(input("Enter the Upper Bound:"))
    acc = 0
    for i in range(lower_bound, upper_bound + 1):
        x = (i ** 2)
        acc = acc + x
    print(acc)


def power():
    base = eval(input("Enter the base:"))
    exp = eval(input("Enter the exponent:"))
    acc = 1
    for i in range(exp):
        acc= acc * base
    print(acc)

