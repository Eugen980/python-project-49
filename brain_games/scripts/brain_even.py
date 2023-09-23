from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for i in range(3):
        x = (randint(1, 100))
        print('Question: ', x)
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and x % 2 == 0 or answer == 'no' and x % 2 != 0:
            print('Correct!')
            count += 1
        elif answer == 'yes' and x % 2 != 0 or answer == 'no' and x % 2 == 0:
            print("""'yes' is wrong answer ;(. Correct answer was 'no'.
            Let's try again,""", name)
            break
        elif answer != 'yes' or answer != 'no':
            print("""'yes' is wrong answer ;(. Correct answer was 'no'.
            Let's try again,""", name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()