"""
Name: Joseph Fagua
lab11.py
"""
import random


# Time to guess the secret words? You have seven guesses!


def read_list(in_file_name):
    infile = open(in_file_name, "r")
    list_words = []
    for line in infile:
        list_words.append(line.strip())
    return list_words


def choose_word(word_list):
    return random.choice(word_list)


def letter_check(random_word, letters,  user_input):
    acc = 0
    for chr in random_word:
        if user_input == chr:
            letters[acc] = user_input
        acc += 1
    return "".join(letters)


def word_spelled(word, ran_word,):
    if word == ran_word:
        return True
    else:
        return False


def play_game():
    words = read_list("wordslist.txt")
    ran_word = choose_word(words)
    letters = []
    for _ in ran_word:
        letters.append('_')
    print(ran_word)
    used_words = []
    print("Guess the secret word? You have 7 guesses!")
    print("".join(letters))
    attempts = 7
    z = True
    while z:
        user_in = input("Guess a letter ")
        used_words.append(user_in)
        word = letter_check(ran_word, letters, user_in)
        print(word)
        if user_in not in ran_word:
            attempts = attempts - 1
            print(attempts, "attempts left")
        if word_spelled(word, ran_word):
            print("congratulations you win")
            z = False
        if attempts == 0:
            print("you lose")
            z = False


def main():
    words = read_list("wordslist.txt")
    ran_word = choose_word(words)
    letters = []
    for _ in ran_word:
        letters.append('_')
    print(ran_word)
    used_words = []
    print("".join(letters))
    while True:
        # print("Guess the secret word? You have",  "guesses!")

        user_in = input("Guess a letter ")
        used_words.append(user_in)
        word = letter_check(ran_word, letters, user_in)
        print(word)
        print(word_spelled(word, ran_word))



play_game()







