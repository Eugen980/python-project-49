from random import randint
from brain_games.engine import run_game
from brain_games.consts import TITLE_PRIME, PRIME_INSTR, NUM_OF_REPEAT


def get_num_and_answer():
    num = randint(1, 100)
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    answer = 'no' if count > 2 or num == 1 else 'yes'
    return num, answer


def run_prime_game():
    print(TITLE_PRIME)
    run_game(get_num_and_answer, NUM_OF_REPEAT, PRIME_INSTR)
