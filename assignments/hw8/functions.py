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


def hit_vertical(cy1, floor, ceiling):

    if cy1 <= floor or cy1 >= ceiling:
        return True


def hit_horizontal(cx1, left_wall, right_wall):
    if cx1 <= left_wall or cx1 >= right_wall:
        return True



