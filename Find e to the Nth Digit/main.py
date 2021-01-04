import math


def eToDigit(digit):
    return f"%.{digit}f" % math.e


print(eToDigit(1))
print(eToDigit(8))
print(eToDigit(28))
