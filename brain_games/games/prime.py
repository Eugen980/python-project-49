from brain_games.random_number import random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_PRIME, PRIME_INSTR


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return 'no' if count > 2 or num == 1 else 'yes'


def get_num_and_answer():
    num = random_number(b=100)
    answer = is_prime(num)
    return num, answer


def run_prime_game():
    print(NAME_GAME_PRIME)
    run_game(get_num_and_answer, PRIME_INSTR)
