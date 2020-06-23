import random


def d8():
    '''this will print the roll of a d8'''
    min = 1
    max = 8

    print(random.randint(min, max))


def DVirgil():
    '''this will print the roll of a d50'''
    min = 1
    max = 50

    print(random.randint(min, max))


def d12():
    '''this will print the roll of a d12'''
    min = 1
    max = 12

    print(random.randint(min, max))


def d10():
    '''this will print the roll of a d10'''
    print(random.randint(1, 10))


def d4():
    '''this will print the roll of a d4'''
    print(random.randint(1, 4))


def d6():
    '''this will print the roll of a d6'''
    print(random.randint(1, 6))


def d20():
    '''this will print the roll of a d20'''
    print(random.randint(1, 20))


def d100():
    '''this will print the roll of a d100'''
    print(random.randint(1, 100))


d4()
d6()
d8()
d10()
d12()
d20()
DVirgil()
d100()
