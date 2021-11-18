"""
Name: Joseph Fagua
lab12.py
"""
from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Joseph"
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def search(lst, value):
    i = 0
    while i < len(lst):
        if value == lst[i]:
            i += 1
            return True
    return False


def gi():
    x = eval(input("enter a # in the range 1 - 10"))
    while x > 10:
        x = eval(input("enter a # in the range 1 - 10"))
    return x


def num_digits():
    num = eval(input("enter a positive integer"))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print("This # has", digits, "digits")
        num = eval(input("enter a positive integer"))


def high_low():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("guess a number between 1-100"))
    while not(guess == num) and not(guesses == 7):
        guesses += 1
        if guess < num:
            print("guess was lower")
        elif guess > num:
            print("guess was higher")
        if not(guess == num) and not(guesses == 7):
            guess = eval(input("guess a number between 1-100"))
    if guess == num:
        print("You win", guesses, "guesses")
    else:
        print("Sorry, ran out of guesses you lose. The number was ", num)


def main():
    read_data("numbers.txt")
    gi()
    num_digits()
    high_low()
main()
