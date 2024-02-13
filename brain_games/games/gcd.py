from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTR
import math


def get_nums_pair_and_gcd():
    first_num, second_num = get_random_number(), get_random_number()
    question = f'{first_num} {second_num}'
    common_divisor = math.gcd(first_num, second_num)
    return question, str(common_divisor)


def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTR)
