import math


def PItoDigit(digit):
    '''  Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number. '''

    return f"%.{digit}f" % math.pi


print(PItoDigit(1))
print(PItoDigit(8))
print(PItoDigit(28))
