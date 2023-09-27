from random import randint
print('brain-prime')
MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def init_game():
    number = randint(1, 100)
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    print('Question: ', number)
    if count > 2:
        answer = 'no'
        return answer
    else:
        answer = 'yes'
        return answer
