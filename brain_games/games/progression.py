from random import randint
print('brain-progression')
MANUAL = 'What number is missing in the progression?'


def init_game():
    sequence = []
    step = randint(1, 5)
    len_seq = 10
    first_element = randint(1, 30)
    random_element = randint(0, len_seq - 1)
    for i in range(first_element, first_element + len_seq):
        sequence.append(str(i*step))
    answer = sequence[random_element]
    sequence[random_element] = '..'
    print(f'Question: {*sequence}')
    return answer
