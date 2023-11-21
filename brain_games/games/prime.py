from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_PRIME, PRIME_INSTR


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    result = 'no' if count > 2 or num == 1 else 'yes'
    return result


def get_num_and_answer():
    num = get_random_number(b=100)
    answer = is_prime(num)
    return num, answer


def run_prime_game():
    run_game(get_num_and_answer, NAME_GAME_PRIME, PRIME_INSTR)
