"""
Name:Joseph Fagua
mean.py

Purpose: Create a python program that outputs the RMS Average, Harmonic Mean, and Geometric mean.

Certificate of Authenticity:
I certify that this assignment is entirely my work.
"""
import math


def main():
    total_values = eval(input("enter the values to be entered:"))
    geo = 1
    rms = 0
    hrm = 0

    for _ in range(total_values):
        values = eval(input("enter value:"))
        geo = geo * values
        rms = rms + values ** 2
        hrm = hrm + (1/values)
    rms_average = math.sqrt(rms / total_values)
    harmonic_average = total_values / hrm
    geometric_mean = geo ** (1 / total_values)
    print(round(rms_average, 3), round(harmonic_average, 3), round(geometric_mean, 3), sep="\n")


if __name__ == '__main__':
    main()
