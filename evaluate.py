from sys import argv

postfix = argv[1]


def evaluate(expression):
    stack = []
    for i in expression:
        if i.isdigit():
            stack.append(i)
        else:
            operand_One = int(stack.pop())
            operator = i
            operand_Two = int(stack.pop())

            operators = {'+': operand_Two + operand_One,
                         '-': operand_Two - operand_One,
                         '*': operand_One * operand_Two,
                         '/': operand_One / operand_Two
                         }

            if operators[operator]:
                stack.append(operators[operator])
            else:
                print(f"Wrong expression '{operator}'!")

    print(f"{stack}")

evaluate(postfix)