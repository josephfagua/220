"""
Name: Joseph Fagua
vigenere.py

purpose: Create a program that takes an input and keyword and returns encoded message

Certificate of Authenticity:
I certify that this assignment is entirely my work.
"""

from graphics import GraphWin, Rectangle, Point, Text, Entry


def main():
    # Create window
    win = GraphWin("Vigenere", 600, 300)
    win.setCoords(0, 0, 30, 30)
    # Create button and Encode message
    button = Rectangle(Point(12.5, 13.3), Point(17.5, 17.7))
    button.draw(win)
    button_message = Text(Point(15, 15.5), "Encode")
    button_message.draw(win)
    # Create message to code and box
    coding_message = Text(Point(4.5, 26), "Message to code")
    coding_message.draw(win)
    input_text_box = Entry(Point(19.1, 26), 40)
    input_text_box.draw(win)
    # Enter Keyword and box
    key_message = Text(Point(5, 21), "Enter Keyword")
    key_message.draw(win)
    input_key_box = Entry(Point(15, 21), 22)
    input_key_box.draw(win)
    # Actual Vigenere cypher encoding

    # un-draw encode button
    win.getMouse()
    button_message.setText(" ")
    button.undraw()
    # Resulting message prompt
    results_message = Text(Point(15, 13), "Resulting Message")
    results_message.draw(win)
    # Draw/Print results of message

    # close the window
    close_window = Text(Point(15, 2), "Click Anywhere to Close Window")
    close_window.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
