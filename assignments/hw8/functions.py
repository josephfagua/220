import math
from graphics import GraphWin, Point, Circle, color_rgb
from random import randint


def getRandomColor():
    cr = randint(0, 255)
    cg = randint(0, 255)
    cb = randint(0, 255)
    setColor = color_rgb(cr, cg, cb)
    return setColor


def getRandom(move_amount):
    negMove = -move_amount
    ranMove = randint(negMove, move_amount)
    return ranMove


def hit_vertical(circle, graphwin):
    r = circle.getRadius()
    ceiling = graphwin.getHeight() - r
    if circle.getCenter().getY() <= r or circle.getCenter().getY() >= ceiling:
        return True
    else:
        return False


def hit_horizontal(circle, graphwin):
    r = circle.getRadius()
    right_wall = graphwin.getWidth() - r
    if circle.getCenter().getX() <= r or circle.getCenter().getX() >= right_wall:
        return True
    else:
        return False


def did_collide(circle1, circle2):
    cordsCB1 = circle1.getCenter()
    cordsCB2 = circle2.getCenter()
    cx1 = int(cordsCB1.getX())
    cy1 = int(cordsCB1.getY())
    cx2 = int(cordsCB2.getX())
    cy2 = int(cordsCB2.getY())
    distance2Points = math.sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)
    if distance2Points < circle1.getRadius() + circle2.getRadius():
        return True
    else:
        return False

