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


def get_random_color():
    cr = randint(0, 255)
    cg = randint(0, 255)
    cb = randint(0, 255)
    return color_rgb(cr, cg, cb)


def get_random(move_amount):
    negMove = -1 * int(move_amount)
    ranMove = randint(negMove, move_amount)
    return ranMove


def main():
    win = GraphWin("Bumper Cars", 600, 900)
    win.setBackground(get_random_color())

    x1 = 300
    y1 = 450
    x2 = 250
    y2 = 300
    dx1 = get_random(15)
    dy1 = get_random(15)
    dx2 = get_random(12)
    dy2 = get_random(12)
    r1 = 40
    r2 = 30
    circle_ball = Circle(Point(x1, y1), r1)
    circle_ball.draw(win)
    circle_ball2 = Circle(Point(x2, y2), r2)
    circle_ball2.draw(win)

    floor = r1
    ceiling = win.getHeight() - r1
    left_wall = r1
    right_wall = win.getWidth() - r1
    floor2 = r2
    ceiling2 = win.getHeight() - r2
    left_wall2 = r2
    right_wall2 = win.getWidth() - r2

    circle_ball.setFill(get_random_color())
    circle_ball.setOutline(get_random_color())
    circle_ball2.setFill(get_random_color())
    circle_ball2.setOutline(get_random_color())

    while True:
        circle_ball.move(dx1, dy1)
        sleep(0.00000000000000001)
        circle_ball2.move(dx2, dy2)
        sleep(0.0001)
        cordsCB1 = circle_ball.getCenter()
        cordsCB2 = circle_ball2.getCenter()
        cx1 = int(cordsCB1.getX())
        cy1 = int(cordsCB1.getY())
        cx2 = int(cordsCB2.getX())
        cy2 = int(cordsCB2.getY())
        distance2Points = math.sqrt((cx2 - cx1)**2 + (cy2 - cy1)**2)
        if circle_ball.getCenter().getY() <= floor or circle_ball.getCenter().getY() >= ceiling:
            dy1 = -dy1
        elif circle_ball.getCenter().getX() <= left_wall or circle_ball.getCenter().getX() >= right_wall:
            dx1 = -dx1
        elif circle_ball2.getCenter().getY() <= floor2 or circle_ball2.getCenter().getY() >= ceiling2:
            dy2 = -dy2
        elif circle_ball2.getCenter().getX() <= left_wall2 or circle_ball2.getCenter().getX() >= right_wall2:
            dx2 = -dx2
        elif distance2Points < r1 + r2:
            dy1 = -dy1
            dx1 = -dx1
            dx2 = -dx2
            dy2 = -dy2


if __name__ == '__main__':
    main()
