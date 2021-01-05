from random import randrange


def coinFlip(num):
    ''' Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads. '''

    coinChoices = ['heads', 'tails']
    outcomes = {}
    for i in range(num):
        # random number that is either 0 or 1
        outcome = coinChoices[randrange(2)]
        if outcome in outcomes.keys():
            outcomes[outcome] += 1
        else:
            outcomes[outcome] = 1
    return outcomes


print(coinFlip(10000))
# takes a second or two to finish depending on your computer
print(coinFlip(1000000))
