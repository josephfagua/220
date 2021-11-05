"""
Name: Joseph Fagua
bumper.py
Purpose: Develop a python program that creates a window that has 2 circles bouncing within

Certification of Authenticity:
I certify that this work is entirely my own.
"""
from random import randint
from time import sleep
from math import sqrt
from graphics import GraphWin, Point, Circle, color_rgb


def get_random_color():
    color_r = randint(0, 255)
    color_g = randint(0, 255)
    color_b = randint(0, 255)
    return color_rgb(color_r, color_g, color_b)


def get_random(move_amount):
    neg_move = -1 * int(move_amount)
    ran_move = randint(neg_move, move_amount)
    return ran_move


def did_collide(circle1, circle2):
    cords_cb1 = circle1.getCenter()
    cords_cb2 = circle2.getCenter()
    cx_1 = int(cords_cb1.getX())
    cy_1 = int(cords_cb1.getY())
    cx_2 = int(cords_cb2.getX())
    cy_2 = int(cords_cb2.getY())
    distance_points = sqrt((cx_2 - cx_1) ** 2 + (cy_2 - cy_1) ** 2)
    return distance_points < circle1.getRadius() + circle2.getRadius()


def hit_horizontal(circle, graphwin):
    radius = circle.getRadius()
    ceiling = graphwin.getHeight() - radius
    return circle.getCenter().getY() <= radius or circle.getCenter().getY() >= ceiling


def hit_vertical(circle, graphwin):
    radius = circle.getRadius()
    right_wall = graphwin.getWidth() - radius
    return circle.getCenter().getX() <= radius or circle.getCenter().getX() >= right_wall


def main():
    win = GraphWin("Bumper Cars", 600, 900)
    win.setBackground(get_random_color())

    x_1 = 300
    y_1 = 450
    x_2 = 250
    y_2 = 300
    dx1 = get_random(15)
    dy1 = get_random(15)
    dx2 = get_random(12)
    dy2 = get_random(12)
    r_1 = 40
    r_2 = 30
    circle_ball = Circle(Point(x_1, y_1), r_1)
    circle_ball.draw(win)
    circle_ball2 = Circle(Point(x_2, y_2), r_2)
    circle_ball2.draw(win)
    circle_ball.setFill(get_random_color())
    circle_ball.setOutline(get_random_color())
    circle_ball2.setFill(get_random_color())
    circle_ball2.setOutline(get_random_color())

    while True:
        circle_ball.move(dx1, dy1)
        sleep(0.00000000000000001)
        circle_ball2.move(dx2, dy2)
        sleep(0.0001)
        if hit_horizontal(circle_ball, win):
            dy1 = -dy1
        elif hit_vertical(circle_ball, win):
            dx1 = -dx1
        elif hit_horizontal(circle_ball2, win):
            dy2 = -dy2
        elif hit_vertical(circle_ball2, win):
            dx2 = -dx2
        elif did_collide(circle_ball, circle_ball2):
            dy1 = -dy1
            dx1 = -dx1
            dx2 = -dx2
            dy2 = -dy2

if __name__ == '__main__':
    main()
