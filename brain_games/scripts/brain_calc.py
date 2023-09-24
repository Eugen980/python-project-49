import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    operation_list = ['+', '-', '*']
    count = 0
    for i in range(3):
        first = random.randint(1, 30)
        second = random.randint(1, 30)
        operation = random.choice(operation_list)
        print('Question: ', first, operation, second)
        answer = prompt.integer('Your answer: ')
        if operation == '+':
            res = first + second
            if res == answer:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'. Let's try again, {name}!")
                break
        elif operation == '-':
            res = first - second
            if res == answer:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'. Let's try again, {name}!")
                break
        elif operation == '*':
            res = first * second
            if res == answer:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'. Let's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
