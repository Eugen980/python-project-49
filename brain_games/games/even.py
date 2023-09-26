from random import randint
print('brain-even')
MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def init_game():
    number = randint(1, 100)
    print('Question: ', number)
    if number % 2 == 0:
        answer = 'yes'
        return answer
    elif number % 2 != 0:
        answer = 'no'
        return answer
