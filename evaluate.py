from sys import argv
import operator

postfix = argv[1]


def evaluate(expression):
    stack = []
    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        else:
            operand_One = stack.pop()
            operand_Two = stack.pop()

            operators = {'+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul,
                         '/': operator.truediv
                         }

            try:
                stack.append(operators[i](operand_Two, operand_One))
            except KeyError:
                print(f"Wrong expression '{i}'!")

    # print(f"{stack}") 
    return stack.pop()

print(evaluate(postfix))