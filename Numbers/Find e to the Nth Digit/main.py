import math


def eToDigit(digit):
    ''' Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go. '''
    
    return f"%.{digit}f" % math.e


print(eToDigit(1))
print(eToDigit(8))
print(eToDigit(28))
