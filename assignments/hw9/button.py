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
        px1 = point.getX()
        py1 = point.getY()
        recp1 = self.shape.getP1
        recp2 = self.shape.getP2
        recp1x = recp1.getX()
        recp1y = recp1.getY()
        recp2x = recp2.getX()
        recp2y = recp2.getY()
        if (recp1x <= px1 <= recp2x) and (recp1y <= py1 <= recp2y):
            return True
        else:
            return False

    def color_button(self, color):
        """This method changes the color of the buttons to either green or red"""
        self.shape.setFill(color)

    def set_label(self, label):
        """This method changes the text of the doors to given string"""
        self.label.setText(label)
