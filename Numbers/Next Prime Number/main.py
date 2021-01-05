def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def findAllPrimeNumbers(num):
    primeNumbers = []
    for i in range(2, num + 1):
        if(isPrime(i)):
            primeNumbers.append(i)
    return primeNumbers


print(findAllPrimeNumbers(100))
