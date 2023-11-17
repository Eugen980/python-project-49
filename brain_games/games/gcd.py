from brain_games.random_number import random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_GCD, GCD_INSTR


def get_common_divisor(a, b):
    res = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return res


def get_nums_and_answer():
    first_num, second_num = random_number(), random_number()
    question = f'{first_num} {second_num}'
    answer = get_common_divisor(first_num, second_num)
    return question, str(answer)


def run_gcd_game():
    print(NAME_GAME_GCD)
    run_game(get_nums_and_answer, GCD_INSTR)
