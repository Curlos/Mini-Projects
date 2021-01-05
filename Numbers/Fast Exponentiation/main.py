import time


def raiseToThePowerOfB(a, b):
    return a ** b


starttime = time.perf_counter()
print(raiseToThePowerOfB(10, 2))
print(time.perf_counter() - starttime)
