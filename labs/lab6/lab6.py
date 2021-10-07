def name_reverse():
    x = input("Enter first and last name")
    x = x.split()
    print(x[1] + ', ' + x[0])


def company_name():
    x = input("Enter three-part internet domain name")
    x = x.split('.')
    print(x[1])


def initials():
    num_names = eval(input("How many names will be input"))
    for i in range(num_names):
        first = input("Enter the first name of student " + str(i + 1) + ":")
        last = input("Enter the last name of student")
        print(first[0] + last[0], end=' ')


def names():
    x = input("Enter list of names")
    x = x.split(', ')
    for name in x:
        parts = name.split()
        print("The initials are " + parts[0][0] + parts[1][0], end='\n')


def thirds():
    n = eval(input("How many sentences will be input"))
    for _ in range(n):
        s = input("Enter sentence")
        print(s[2::3])


def word_average():
    x = input("Enter sentence")
    x = x.split()
    acc = 0
    for word in x:
        acc = acc + len(word)
    print(acc / len(x))


def pig_latin():
    x = input("Enter sentence to convert")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay", end=' ')

# name_reverse()
# company_name()
# initials()
# names()
# thirds()
# word_average()
pig_latin()
