def calculateFactorialLoop(num):
    ''' Calculates factorial of a positive integer using loops '''

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def calculateFactorialRec(num):
    ''' Calculates factorial of a positive integer using recursion '''

    if num == 1:
        return 1
    else:
        print(f"num: {num}")
        return calculateFactorialRec(num - 1) * num


print(calculateFactorialRec(10))
