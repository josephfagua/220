"""
Name: Joseph Fagua
button.py
Purpose: Develop a python program that creates a button class to be used in three_door_game.py

Certification of Authenticity:
I certify that this work is entirely my own.
"""
from graphics import Text


class Button:
    """This class creates a Button with a label at the center"""
    def __init__(self, rectangle_shape, string_label):
        """This constructs the button class"""
        self.shape = rectangle_shape
        self.text = string_label

    def get_label(self):
        """This method returns the text of the button"""
        return self.text

    def draw(self, win):
        """This method draws the button with text on it to the window"""
        p_1 = self.shape.getCenter()
        self.text = Text(p_1, self.text)
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """This method undraws the button with text on it to the window"""
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """This method checks to see if the mouse click in the region"""
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        width = abs(p_1.getX() - p_2.getX())
        height = abs(p_1.getY() - p_2.getY())
        x_1 = point.getX()
        y_1 = point.getY()
        d_x = abs(self.shape.getCenter().getX() - x_1)
        d_y = abs(self.shape.getCenter().getY() - y_1)
        if d_x <= width/2 and d_y <= height/2:
            return True
        return False

    def color_button(self, color):
        """This method changes the color of the buttons to either green or red"""
        self.shape.setFill(color)

    def set_label(self, label):
        """This method changes the text of the doors to given string"""
        self.text.setText(label)
