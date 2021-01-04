import re

def countWords(s):
    ''' Counts the number of individual words in a string assuming each word is separated by a space.'''

    wordCount = 0

    for word in s.split():
        wordCount += 1

    return wordCount


def countWordsFromFile(filename):
    wordCount = 0

    with open(filename, 'r') as f:
        for line in f.readlines():
            for word in line.split():
                wordRe = re.split(', |_|-|!', word)
                for word in wordRe:
                    wordCount += 1
    return wordCount


print(countWords('The isalpha() method returns True if all the characters are alphabet letters (a-z).'))
print(countWordsFromFile('swd1_5-74.txt'))
