"""
Name: Joseph Fagua
greeting.py

purpose: Create a python program that draws a heart and runs
an animation of an arrow piercing the heart

Certification of Authenticity:
I certify that this assignment is entirely my work.
"""

from graphics import GraphWin, Circle, Polygon, Point, Text, Line, update


def main():
    win = GraphWin("Greeting", 400, 400, autoflush=True)
    win.setCoords(0, 0, 100, 100)
    warning = Text(Point(50, 95), "click anywhere")
    warning.draw(win)

    # Circle 1
    left_circle = Circle(Point(40, 70), 15)
    left_circle.setFill("pink")
    left_circle.setOutline("pink")
    left_circle.draw(win)
    # Circle 2
    right_circle = Circle(Point(60, 70), 15)
    right_circle.setFill("pink")
    right_circle.setOutline("pink")
    right_circle.draw(win)
    # Polygon
    polygon_one = Polygon(Point(26.85, 63), Point(73.28, 63), Point(50, 25))
    polygon_one.setOutline("pink")
    polygon_one.setFill("pink")
    polygon_one.draw(win)
    # undraws message click anywhere
    # Happy Valentines Day Message
    message = Text(Point(50, 70), "Happy Valentines Day")
    message.draw(win)
    # undraws message click anywhere and Happy valentine
    win.getMouse()
    warning.undraw()
    message.undraw()
    # Arrow
    for _ in range(45):
        arrow = Line(Point(0, 25), Point(60, 60))
        arrow.setArrow("last")
        arrow.draw(win)
        arrow.undraw()
        update(60)
    arrow.move(21, 12)
    arrow.draw(win)
    # I need to replace the
    closing = Text(Point(50, 10), "Click anywhere to close")
    closing.draw(win)
    # close window on click
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
