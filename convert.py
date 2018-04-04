import math

def __main__():
    inputString = input("Please insert the number you want to convert: ")
    inputBase = input("In what system do you want to convert (number from 2 - 9) :")
    inputNumber = int(inputString)
    base = int(inputBase)

    convertedNumber = convertIntoBase(base, inputNumber)

    print ("Decimal: " + inputString)
    print (str(base) + "-base:  " + str(convertedNumber))

def convertIntoBase(baseInteger, number):
    generatedList = []
    while (number > 0):
        generatedList.append(number % baseInteger)
        number = math.floor(number / baseInteger)
    newNumber = 0
    position = 0
    for digit in generatedList:
        newNumber += digit*(10**position)
        position += 1
    return newNumber

__main__()
