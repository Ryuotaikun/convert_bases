import math

def __main__():
    inputString = input("Please insert the number you want to convert: ")
    inputStartingBase = input("What base is your number (number from 2-10): ")
    inputWantedBase = input("In what base do you want to convert: ")

    numberToConvert = int(inputString)
    startingBase = int(inputStartingBase)
    wantedBase = int(inputWantedBase)

    print (str(startingBase) + "-base:  " + inputString)

    if (startingBase != 10):
        numberToConvert = convertIntoDecimal(startingBase, numberToConvert)

    if (wantedBase != startingBase):
        if (wantedBase != 10):
            print ("Decimal: " + str(numberToConvert))
            convertedNumberString = convertIntoBase(wantedBase, numberToConvert)
        else:
            convertedNumberString = str(numberToConvert)
        print (str(wantedBase) + "-base:  " + convertedNumberString)
    else:
        print ("not very usefull converting into the same system, is it?")

def convertIntoDecimal(base, number):
    numberString = str(number)
    decimalNumber = 0
    power = len(numberString)-1
    for digit in numberString:
        decimalNumber += int(digit)*base**power
        power -= 1
    return decimalNumber

def convertIntoBase(base, number):
    generatedList = []
    while (number > 0):
        generatedList.append(number % base)
        number = math.floor(number / base)
    newNumberString = ""
    for digit in reversed(generatedList):
        if digit < 10:
            newNumberString += chr(48+digit)
        else:
            newNumberString += chr(55+digit)
    return newNumberString

__main__()
