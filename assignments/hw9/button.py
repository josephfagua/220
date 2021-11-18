from graphics import *


class Button:
    def __init__(self, rectangle_shape, string_label):
        self.shape = rectangle_shape
        self.label = string_label

    def get_label(self):
        """This method returns the text of the button"""
        return self.label

    def draw(self, win):
        """This method draws the button with text on it to the window"""
        p1 = self.shape.getCenter()
        self.label = Text(p1, self.label)
        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self):
        """This method undraws the button with text on it to the window"""
        self.shape.undraw()
        self.label.undraw()

    def is_clicked(self, point):
        """This method checks to see if the mouse click in the region"""
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        w = abs(p1.getX() - p2.getX())
        h = abs(p1.getY() - p2.getY())
        x = point.getX()
        y = point.getY()
        dx = abs(self.shape.getCenter().getX() - x)
        dy = abs(self.shape.getCenter().getY() - y)
        if dx <= w/2 and dy <= h/2:
            return True
        else:
            return False

    def color_button(self, color):
        """This method changes the color of the buttons to either green or red"""
        self.shape.setFill(color)

    def set_label(self, label):
        """This method changes the text of the doors to given string"""
        self.label.setText(label)
