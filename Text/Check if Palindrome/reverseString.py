def reverseString(s):
    ''' Enter a string and the program will reverse it and print it out. '''
    reversedString = ''
    charArray = []

    for i in range(len(s) - 1, -1, -1):
        charArray.append(s[i])

    return reversedString.join(charArray)
