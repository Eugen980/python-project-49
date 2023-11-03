from random import randint
from brain_games.engine import run_game
from brain_games.games.consts import TITLE_EVEN, EVEN_INSTR


def get_num_and_answer():
    num = randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    return num, answer


def run_even_game():
    run_game(get_num_and_answer, TITLE_EVEN, EVEN_INSTR)
