import random
from brain_games.engine import run_game
from brain_games.consts import TITLE_CALC, CALC_INSTR, NUM_OF_ROUND, OPERATION


def get_operation(f_num, operation, sec_num):
    if operation == '+':
        return f_num + sec_num
    elif operation == '-':
        return f_num - sec_num
    elif operation == '*':
        return f_num * sec_num


def get_nums_and_answer():
    first, second = random.randint(1, 30), random.randint(1, 30)
    operation = random.choice(OPERATION)
    question = f'{first} {operation} {second}'
    answer = get_operation(first, operation, second)
    return question, str(answer)


def run_calc_game():
    print(TITLE_CALC)
    run_game(get_nums_and_answer, NUM_OF_ROUND, CALC_INSTR)
