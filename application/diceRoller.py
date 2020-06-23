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


def main():
    dieChoice = input("Please enter the die you would like to roll: d")
    numberChoice = input("Please enter how many you would like to roll: ")
    if int(dieChoice) == 4:
        for x in numberChoice:
            d4()
    elif int(dieChoice) == 6:
        for x in numberChoice:
            d6()
    elif int(dieChoice) == 8:
        for x in numberChoice:
            d8()
    elif int(dieChoice) == 10:
        for x in numberChoice:
            d10()
    elif int(dieChoice) == 12:
        for x in numberChoice:
            d12()
    elif int(dieChoice) == 20:
        for x in numberChoice:
            d20()
    elif int(dieChoice) == 50:
        for x in numberChoice:
            DVirgil()
    elif int(dieChoice) == 100:
        for x in numberChoice:
            d100()
    else:
        print("Nah bro")

main()
