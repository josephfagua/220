"""
Name: Joseph Fagua
lab13.py
"""
from random import randint


def is_in_binary(search, values):
    mid = len(values)//2
    while search != values[mid] and len(values) != 1:
        if search < values[mid]:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values)//2
    if search == values[mid]:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def get_area(rect):
    return randint(1, 100)


def rect_sort(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)


def trades(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    pos = 1
    for i in range(len(data)):
        pos += 1
        print(data[i])
        if int(data[i]) > 830:
            print("Alert! " + str(pos) + "th second")
        elif int(data[i]) > 500:
            print("Warning! " + str(pos) + "th second")


def main():
    trades("trades.txt")


main()
