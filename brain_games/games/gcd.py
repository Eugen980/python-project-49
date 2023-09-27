from random import randint
print('brain-gcd')
MANUAL = 'Find the greatest common divisor of given numbers.'


def init_game():
    first = randint(1, 20)
    second = randint(1, 20)
    com_div = 1
    print(f'Question: {first} {second}')
    for i in range(1, min(first, second) + 1):
        if first % i == 0 and second % i == 0:
            com_div = i
    answer = com_div
    return str(answer)
