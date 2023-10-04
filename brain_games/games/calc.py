from random import randint, choice
print('brain-calc')
MANUAL = 'What is the result of the expression?'


def init_game():
    operation_list = ('+', '-', '*')
    first = randint(1, 30)
    second = randint(1, 30)
    operation = choice(operation_list)
    print(f'Question: <first> <operation> <second>')
    if operation == '+':
        answer = str(first + second)
        return answer
    elif operation == '-':
        answer = str(first - second)
        return answer
    elif operation == '*':
        answer = str(first * second)
        return answer
