from button import Button
from graphics import GraphWin, Rectangle, Point, Text


def three_door_game():
    win = GraphWin("Three Door Game", 350, 250)
    win.setCoords(0, 0, 30, 50)
    top_message = Text(Point(15, 40), "I have a secret door")
    """Doors"""
    box1 = Rectangle(Point(2.5, 15), Point(8.5, 26))
    box2 = Rectangle(Point(12, 15), Point(18, 26))
    box3 = Rectangle(Point(21.5, 15), Point(27.5, 26))
    door1 = Button(box1, "Door 1")
    door2 = Button(box2, "Door 2")
    door3 = Button(box3, "Door 3")
    """Drawing Doors and Text"""
    top_message.draw(win)
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)
    bot_message = Text(Point(15, 2), "click to choose my door")
    bot_message.draw(win)

    game = True
    while game:
        point = win.checkMouse()
        win.getMouse()
        print(point)





if __name__ == '__main__':
    three_door_game()
