"""
Name: <your name goes here – first and last>
Partner: <your partner's name goes here – first and last>
<ProgramName>.py
"""
import math


def cash_conversion():
    integer = eval(input("Enter an integer"))
    print("{:.2f}".format(integer))


def encode():
    s = input("Enter the message to be encoded")
    k = eval(input("Enter inter key value"))
    acc = " "
    for c in s:
        i = ord(c)
        ks = k + i
        c = chr(ks)
        acc = acc + c
    print(acc)


def sphere_area(radius):
    sa = 4 * math.pi * radius ** 2
    return sa


def sphere_volume(radius):
    v = (4/3) * math.pi * radius**3
    return v


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i**3)
    return acc


def encode_better():
    s = input("Enter the message to be encoded")
    k = input("Enter the cipher key message")
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        ck = key + c
        c = chr(ck)
        acc = acc + c
    print(acc)


def main():
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(3))
    print(sum_n_cubes(3))
    encode_better()
    encode()
    cash_conversion()



