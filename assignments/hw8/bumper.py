"""
Name: Joseph Fagua
bumper.py
Purpose: Develop a python program that creates a window that has 2 circles bouncing within

Certification of Authenticity:
I certify that this work is entirely my own.
"""
from graphics import GraphWin, Point, Circle, color_rgb
from random import randint
from time import sleep
import math


def getRandomColor():
    cr = randint(0, 255)
    cg = randint(0, 255)
    cb = randint(0, 255)
    return color_rgb(cr, cg, cb)


def getRandom(move_amount):
    negMove = -1 * int(move_amount)
    ranMove = randint(negMove, move_amount)
    return ranMove


# def hitVertical(circleBall, graphwin):
#     floor = graphwin
#     if circleBall.getCenter().getY() <= floor or circleBall.getCenter().getY() >= ceiling:
#         return True
#     else:
#         return False


def main():
    win = GraphWin("Bumper Cars", 600, 900)
    win.setBackground(getRandomColor())

    x1 = 300
    y1 = 450
    x2 = 250
    y2 = 300
    dx1 = getRandom(15)
    dy1 = getRandom(15)
    dx2 = getRandom(12)
    dy2 = getRandom(12)
    r1 = 40
    r2 = 30
    circleBall = Circle(Point(x1, y1), r1)
    circleBall.draw(win)
    circleBall2 = Circle(Point(x2, y2), r2)
    circleBall2.draw(win)

    floor = r1
    ceiling = win.getHeight() - r1
    leftWall = r1
    rightWall = win.getWidth() - r1
    floor2 = r2
    ceiling2 = win.getHeight() - r2
    leftWall2 = r2
    rightWall2 = win.getWidth() - r2

    circleBall.setFill(getRandomColor())
    circleBall.setOutline(getRandomColor())
    circleBall2.setFill(getRandomColor())
    circleBall2.setOutline(getRandomColor())

    while True:
        circleBall.move(dx1, dy1)
        sleep(0.00000000000000001)
        circleBall2.move(dx2, dy2)
        sleep(0.0001)
        cordsCB1 = circleBall.getCenter()
        cordsCB2 = circleBall2.getCenter()
        cx1 = cordsCB1.getX()
        cy1 = cordsCB1.getY()
        cx2 = cordsCB2.getX()
        cy2 = cordsCB2.getY()
        distance2Points = math.sqrt((cx2 - cx1)**2 + (cy2 - cy1)**2)

        if circleBall.getCenter().getY() <= floor or circleBall.getCenter().getY() >= ceiling:
            dy1 = -dy1
        elif circleBall.getCenter().getX() <= leftWall or circleBall.getCenter().getX() >= rightWall:
            dx1 = -dx1
        elif circleBall2.getCenter().getY() <= floor2 or circleBall2.getCenter().getY() >= ceiling2:
            dy2 = -dy2
        elif circleBall2.getCenter().getX() <= leftWall2 or circleBall2.getCenter().getX() >= rightWall2:
            dx2 = -dx2
        elif distance2Points < r1 + r2:
            # the circles are bouncing in the opposite direction in which they came
            # however they do not do in the direction that the other circle bounces them.
            dy1 = -dy1
            dx1 = -dx1
            dx2 = -dx2
            dy2 = -dy2


if __name__ == '__main__':
    main()
