from button import Button
from random import choice, randrange
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
    option = randrange(1, 4)

    click = win.getMouse()
    if door1.is_clicked(click):
        if option == 1:
            door1.color_button("green")
            top_message.setText("You Win!")
            bot_message.setText("click to close")
        if option != 1:
            door1.color_button("red")
            top_message.setText("You Lose!")
            bot_message.setText("Door " + str(option) + " is the secret door")
    win.getMouse()

if __name__ == '__main__':
    three_door_game()
