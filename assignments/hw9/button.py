from graphics import Text


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
        pass

    def color_button(self, color):
        """This method changes the color of the buttons to either green or red"""
        self.shape.setFill(color)

    def set_label(self, label):
        self.label.setText(label)
