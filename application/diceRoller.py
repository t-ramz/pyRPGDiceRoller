import random
import re


class Dice():
    def __init__(self, max):
        self.max = max

    def Roll(self):
        print(random.randint(1, self.max))


def main():
    '''Regex for matching proper command string'''
    command = re.compile(r"\/roll\s+[0-9]+d[0-9]+$")

    '''Regex for extractring valuable information from input string'''
    subtract = re.compile(r"\/roll\s+")

    ''''Prompt for the command'''
    print("Type commmand to roll dice.")
    print("Ex: /roll 3d10")
    inputString = input()

    if command.match(inputString):
        '''Extract information from input string'''
        subString = re.sub((subtract), '', inputString)

        '''Categorize valuable information'''
        splitString = subString.split("d")
        numToRoll = int(subString[0])
        dice = Dice(int(splitString[1]))

        '''Execute the command'''
        for i in range(numToRoll):
            dice.Roll()
    else:
        print("Command not found")


if __name__ == '__main__':
    main()
