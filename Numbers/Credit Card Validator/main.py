from reverseString import reverseString
from functools import reduce


def validateCreditCard(creditCardNum):
    ''' Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum). '''

    cardNum = str(creditCardNum).replace(' ', '')
    cardNumNoLastDigit = cardNum[:-1]
    print(cardNum)
    reversedDigitsStr = reverseString(cardNumNoLastDigit)
    digits = [int(char) for char in reversedDigitsStr]
    print([int(char) for char in cardNum])
    print(digits)
    digitsArray = []

    for i in range(len(reversedDigitsStr)):
        numDigit = int(reversedDigitsStr[i])
        numDigitDoubled = numDigit * 2

        if i % 2 == 0:
            '''if(numDigitDoubled > 9):
                #numDigitDoubled -= 9 '''
            digitsArray.append(numDigitDoubled)
        else:
            '''if(numDigit > 9):
                #numDigit -= 9 '''
            digitsArray.append(numDigit)

    summedUpDigits = reduce(lambda x, y: x + y, digitsArray)
    mod10 = summedUpDigits % 10
    lastDigit = int(cardNum[-1])

    print((digitsArray, summedUpDigits, mod10, lastDigit))

    return mod10 == lastDigit


def findCreditCardIssuer(creditCardNum):
    cardNum = str(creditCardNum).replace(' ', '')
    print(validateCreditCard(cardNum))
    if validateCreditCard(cardNum):
        if len(cardNum) == 16:
            if cardNum.startswith('4'):
                print('VISA')
    return len(cardNum)


print(validateCreditCard('4024007196561053'))
# print(findCreditCardIssuer('4024007196561053'))  # visa
