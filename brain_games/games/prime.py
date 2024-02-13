from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import PRIME_INSTR


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return not (count > 2 or num == 1)


def get_num_and_answer():
    num = get_random_number(end=100)
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer


def run_prime_game():
    run_game(get_num_and_answer, PRIME_INSTR)
