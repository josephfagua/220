"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
import math
from graphics import GraphWin, Circle, Text, Point


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList = float(strList[i])


def write_sum_of_squares():
    ifn = input("Name of input file")
    infile = open(ifn, 'r')
    outfile = open("output.txt", 'w+')
    for line in infile:
        newLine = line.split(' ')
        toNumbers(newLine)
        squareEach(newLine)
        Sum = sumList(newLine)
        outfile.write("Sum of Squares =" + str(Sum))


def starter():
    weight = eval(input("enter players weight"))
    wins = eval(input("enter the players wins"))
    if 150 <= weight < 160 and wins >= 5:
        print("is starter")
    elif weight > 199 or wins > 20:
        print("is starter")
    else:
        print("is not starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circleOverlap():
    win = GraphWin("CircleOverlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius_two = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circleTwo = Circle(p4, radius_two)
    circleTwo.draw(win)
    if math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2) < radius + radius_two:
        pos_message = Text(Point(200, 200), "The Circles overlap")
        pos_message.draw(win)
        win.getMouse()
    else:
        message = Text(Point(200, 200), "The Circles do not overlap")
        message.draw(win)
        win.getMouse()


def main():
    # write_sum_of_squares()
    # starter()
    # leapYear(2000)
    circleOverlap()


main()
