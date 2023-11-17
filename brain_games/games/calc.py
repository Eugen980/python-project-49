import random
from brain_games.random_number import random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_CALC, CALC_INSTR, OPERATIONS


def get_result_of_operation(first_num, operation, second_num):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num


def get_expression_and_answer():
    first, second = random_number(), random_number()
    operation = random.choice(OPERATIONS)
    question = f'{first} {operation} {second}'
    answer = get_result_of_operation(first, operation, second)
    return question, str(answer)


def run_calc_game():
    print(NAME_GAME_CALC)
    run_game(get_expression_and_answer, CALC_INSTR)
