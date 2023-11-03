from random import randint
from brain_games.engine import run_game
from brain_games.games.consts import TITLE_GCD, GCD_INSTR


def get_nums_and_answer():
    first = randint(1, 20)
    second = randint(1, 20)
    com_div = 1
    question = str(f'{first} {second}')
    for i in range(1, min(first, second) + 1):
        if first % i == 0 and second % i == 0:
            com_div = i
    answer = com_div
    return question, str(answer)


def run_gcd_game():
    run_game(get_nums_and_answer, TITLE_GCD, GCD_INSTR)
