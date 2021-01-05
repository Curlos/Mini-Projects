def reverseString(s):
    ''' Enter a string and the program will reverse it and print it out. '''
    reversedString = ''
    charArray = []

    for i in range(len(s) - 1, -1, -1):
        charArray.append(s[i])

    return reversedString.join(charArray)


print(reverseString('Write a program that prints the numbers from 1 to 100.'))
