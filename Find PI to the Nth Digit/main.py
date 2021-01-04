import math


def PItoDigit(digit):
    return f"%.{digit}f" % math.pi


print(PItoDigit(1))
print(PItoDigit(8))
print(PItoDigit(28))
