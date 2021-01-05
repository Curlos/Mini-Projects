from reverseString import reverseString


def isPalindrome(s):
    ''' Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar” '''

    if s == reverseString(s):
        return True
    return False


print(isPalindrome('racecar'))
print(isPalindrome('carlos'))
