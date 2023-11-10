import random
from brain_games.engine import run_game
from brain_games.consts import TITLE_PRIME, PRIME_INSTR, NUM_OF_REPEAT


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return 'no' if count > 2 or num == 1 else 'yes'


def get_num_and_answer():
    num = random.randint(1, 100)
    answer = is_prime(num)
    return num, answer


def run_prime_game():
    print(TITLE_PRIME)
    run_game(get_num_and_answer, NUM_OF_REPEAT, PRIME_INSTR)
