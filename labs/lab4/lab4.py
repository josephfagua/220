"""
Name: Joseph Fagua
lab4.py
"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a Rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click corners of Rectangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    r.draw(win)

    area = length * width
    area_txt = Text(Point(200, 350), "The area is " + str(area))
    area_txt.draw(win)

    perimeter = 2 * (length + width)
    perimeter_txt = Text(Point(200, 370), "The perimeter is " + str(perimeter))
    perimeter_txt.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click center point and circumference point")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    c = Circle(p1, d)
    c.draw(win)

    radius = d
    radius_txt = Text(Point(200, 350), "The radius is " + str(radius))
    radius_txt.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4 * ((-1) ** i)
        denominator = 1 + 2 * i
        fraction = num / denominator
        acc = acc + fraction
    print(math.pi - acc)


def main():
    squares()
    # rectangle()
    # circle()
    # pi2()


main()
