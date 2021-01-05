def countVowels(s):
    ''' Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found. '''

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0

    for char in s:
        if char.lower() in vowels:
            vowelCount += 1
    return vowelCount


print(countVowels('With floating point representation, your rounded version is the same number. Since computers are binary, they store floating point numbers as an integer and then divide it by a power of two so 13.95 will be represented in a similar fashion to 125650429603636838/(2**53).'))  # Should print 77 (77 vowels in this string)
