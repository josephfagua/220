"""
Name: Joseph Fagua
label.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the total shots: "))
    # eval(input(insert here) will prompt the program user to give the entered action found in the parenthesis so in
    # this example the total shots made by a player
    shots_made = eval(input("Enter the shots made: "))
    shooting_percentage = (shots_made / total_shots) * 100
    print("shooting_percentage=", shooting_percentage)


def coffee():
    pounds_of_coffee_purchased = eval(input("Enter the total pounds of coffee purchased:"))
    # pounds_of_coffee becomes the x variable in the equation of y=mx+b
    total_cost = (10.50 * pounds_of_coffee_purchased) + (0.86 * pounds_of_coffee_purchased) + 1.50
    print("total_cost=", total_cost)


def kilometers_to_miles():
    kilometers_traveled = eval(input("Enter the total number of kilometers traveled:"))
    miles_traveled = kilometers_traveled / 1.61
    print("miles_traveled=", miles_traveled)
