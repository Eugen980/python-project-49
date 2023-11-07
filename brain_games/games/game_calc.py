from random import randint, choice
from brain_games.engine import run_game
from brain_games.consts import TITLE_CALC, CALC_INSTR, NUM_OF_REPEAT


def get_nums_and_answer():
    operation_list = ('+', '-', '*')
    first = randint(1, 30)
    second = randint(1, 30)
    operation = choice(operation_list)
    question = str(f'{first} {operation} {second}')
    if operation == '+':
        answer = str(first + second)
        return question, answer
    elif operation == '-':
        answer = str(first - second)
        return question, answer
    elif operation == '*':
        answer = str(first * second)
        return question, answer


def run_calc_game():
    print(TITLE_CALC)
    run_game(get_nums_and_answer, NUM_OF_REPEAT, CALC_INSTR)
