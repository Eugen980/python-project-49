from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTR


def get_common_divisor(a, b):
    res = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return res


def get_nums_and_common_divisor():
    first_num, second_num = get_random_number(), get_random_number()
    question = f'{first_num} {second_num}'
    common_divisor = get_common_divisor(first_num, second_num)
    return question, str(common_divisor)


def run_gcd_game():
    run_game(get_nums_and_common_divisor, GCD_INSTR)
