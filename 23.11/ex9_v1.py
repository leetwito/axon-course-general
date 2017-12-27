import numpy
import random
import string

def StrengthInput ():
    option = raw_input("Enter (S)trong/(W)eak: ")
    # passLength=0

    if option == "S" or option == 'W':
        return option
    else:
        return 'E'

# def GenerateStrongPass():

def nextBit():
    return chr(random.randint(33, 122))


def GenerateWeakPass():
    wordsList = ['axon', 'vision', 'Maor', 'lEe']
    wordnum1 = random.randint(0, 3)
    wordnum2 = random.randint(0, 3)

    myWeakPassword = wordsList[wordnum1]+wordsList[wordnum2]
    return myWeakPassword


def GenerateStrongPass():
    myStrongPassword = ''
    for i in range(0,12):
        myStrongPassword = myStrongPassword + nextBit()
    return myStrongPassword

def main ():
    passStrength = StrengthInput()

    if passStrength == 'S':
        print(GenerateStrongPass())
    elif passStrength == 'W':
        print(GenerateWeakPass())
    else:
        print('Error')


if __name__== "__main__":
    main()




