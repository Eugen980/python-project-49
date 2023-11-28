import random
from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import CALC_INSTR, MATH_SIGNS


def get_result_by_math_sign(first_num, math_sign, second_num):
    match math_sign:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def get_math_expression_and_result():
    first_num, second_num = get_random_number(), get_random_number()
    math_sign = random.choice(MATH_SIGNS)
    math_expression = f'{first_num} {math_sign} {second_num}'
    result = get_result_by_math_sign(first_num, math_sign, second_num)
    return math_expression, str(result)


def run_calc_game():
    run_game(get_math_expression_and_result, CALC_INSTR)
