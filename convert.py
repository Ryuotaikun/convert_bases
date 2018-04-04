import math

def __main__():
    inputString = input("Please insert the number you want to convert: ")
    inputStartingBase = input("In what system do you want to convert: ")
    inputNumber = int(inputString)
    base = int(inputStartingBase)

    convertedNumberString = convertIntoBase(base, inputNumber)

    print ("Decimal: " + inputString)
    print (str(base) + "-base:  " + convertedNumberString)

def convertIntoBase(baseInteger, number):
    generatedList = []
    while (number > 0):
        generatedList.append(number % baseInteger)
        number = math.floor(number / baseInteger)
    newNumberString = ""
    for digit in reversed(generatedList):
        if digit < 10:
            newNumberString += chr(48+digit)
        else:
            newNumberString += chr(55+digit)
    return newNumberString

__main__()
