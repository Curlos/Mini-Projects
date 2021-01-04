from reverseString import reverseString


def isPalindrome(s):
    if s == reverseString(s):
        return True
    return False


print(isPalindrome('racecar'))
print(isPalindrome('carlos'))
