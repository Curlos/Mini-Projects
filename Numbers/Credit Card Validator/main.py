from reverseString import reverseString
from functools import reduce


def validateCreditCard(cardNum):
    ''' Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum). '''

    cardNumNoLastDigit = cardNum[:-1]
    reversedDigitsStr = reverseString(cardNumNoLastDigit)
    digits = [int(char) for char in reversedDigitsStr]
    digitsArray = []
    print(digits)

    for i in range(len(reversedDigitsStr)):
        numDigit = int(reversedDigitsStr[i])
        numDigitDoubled = numDigit * 2

        if i % 2 == 0:
            if(numDigitDoubled > 9):
                numDigitDoubled -= 9
            digitsArray.append(numDigitDoubled)
        else:
            if(numDigit > 9):
                numDigit -= 9
            digitsArray.append(numDigit)

    summedUpDigits = reduce(lambda x, y: x + y, digitsArray)
    mod10 = summedUpDigits % 10
    lastDigit = int(cardNum[-1])

    return mod10 == lastDigit


print(validateCreditCard('4556737586899855'))
