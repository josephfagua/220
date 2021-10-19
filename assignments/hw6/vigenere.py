"""
Name: Joseph Fagua
vigenere.py

purpose: Create a program that takes an input and keyword and returns encoded message

Certificate of Authenticity:
I certify that this assignment is entirely my work.
"""

from graphics import GraphWin, Rectangle, Point, Text, Entry


def code(message, keyword):
    s = message
    k = keyword
    acc = " "
    k = k.upper()
    s = s.upper()
    s = s.split(" ")
    k = k.split(" ")
    s = "".join(s)
    k = "".join(k)
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        ord_c = ord(c) - 65
        ord_key = ord(key) - 65
        ck = (ord_key + ord_c) % 26
        cn = ck + 65
        ch = chr(cn)
        acc = acc + ch
    return acc


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
    # un-draw encode button
    win.getMouse()
    button_message.setText(" ")
    button.undraw()
    # Resulting message prompt
    results_message = Text(Point(15, 13), "Resulting Message")
    results_message.draw(win)
    # Draw/Print results of message
    text_message = input_text_box.getText()
    text_keyword = input_key_box.getText()
    tm = eval(text_message)
    tk = eval(text_keyword)
    encoded_result = Text(Point(15, 11), code(tm, tk))
    encoded_result.draw(win)
    # close the window
    close_window = Text(Point(15, 2), "Click Anywhere to Close Window")
    close_window.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
