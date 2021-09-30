"""
Name: Joseph Fagua
lab5.py
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    #draws triangle
    P1 = win.getMouse()
    P2 = win.getMouse()
    P3 = win.getMouse()
    Triangle = Polygon(P1, P2, P3)
    Triangle.draw(win)

    x1 = P1.getX()
    x2 = P2.getX()
    x3 = P3.getX()
    y1 = P1.getY()
    y2 = P2.getY()
    y3 = P3.getY()
    dx = x2 - x1
    dx2 = x3 - x2
    dx3 = x3 - x1
    dy = y2 - y1
    dy2 = y3 - y2
    dy3 = y3 - y1
    a = math.sqrt((dx**2) + dy**2)
    b = math.sqrt((dx2**2) + dy2**2)
    c = math.sqrt((dx3**2) + dy3**2)
    s = (a + b + c) / 2
    perimeter = a + b + c
    perimeter_txt = Text(Point(250, 450), "perimeter is " + str(round(perimeter, 3)))
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    area_txt = Text(Point(250, 400), "area is " + str(round(area, 3)))
    perimeter_txt.draw(win)
    area_txt.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # code goes here
    red_box = Entry(Point(win_width / 2 , win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = input('enter a string')
    print(s[0])
    print(s[-1])
    print(s[1:5])
    print(s[1] + s[-1])
    print(s[:3] * 10)
    for i in range(len(s)):
        c = s[i]
        print(c)
    len(s)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    series = eval(input("Enter the terms"))
    acc = 0
    for i in range(series):
        y = 2 + 2 * (i % 3)
        print(y, end=' ')
        acc = acc + y
    print("sum", acc)


def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    another_series()


main()

