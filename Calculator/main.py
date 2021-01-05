import re
import operator


class SimpleCalculator():
    def __init__(self):
        self.ops = {"+": operator.add, "-": operator.sub,
                    "*": operator.mul, "x": operator.mul, "/": operator.truediv}

    def parseInput(self, input):
        mo = re.search(
            r'(\d+)\s*([+\/*x-])\s*(\d+)', input)

        if mo is None:
            print('Invalid expression!')
        else:
            num1 = mo.group(1).strip()
            operator = mo.group(2).strip()
            num2 = mo.group(3).strip()
            return (num1, operator, num2)

    def calculate(self, input='2x2'):
        try:
            userInput = self.parseInput(input)
            num1 = int(userInput[0])
            operator = userInput[1]
            num2 = int(userInput[2])

            return self.ops[operator](num1, num2)
        except TypeError:
            print('Input did not match the correct format (2 + 2).')


calculator = SimpleCalculator()

# sample input: '300 * 10', sample output: 3000
print(calculator.calculate(input('Enter an expression: ')))
