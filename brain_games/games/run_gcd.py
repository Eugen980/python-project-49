import random
from brain_games.engine import run_game
from brain_games.consts import TITLE_GCD, GCD_INSTR, NUM_OF_ROUND


def get_common_divisor(a, b):
    res = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return res


def get_nums_and_answer():
    first, second = random.randint(1, 20), random.randint(1, 20)
    question = f'{first} {second}'
    answer = get_common_divisor(first, second)
    return question, str(answer)


def run_gcd_game():
    print(TITLE_GCD)
    run_game(get_nums_and_answer, NUM_OF_ROUND, GCD_INSTR)
