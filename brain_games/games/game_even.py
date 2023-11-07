from random import randint
from brain_games.engine import run_game
from brain_games.consts import TITLE_EVEN, EVEN_INSTR, NUM_OF_REPEAT


def get_num_and_answer():
    num = randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    return num, answer


def run_even_game():
    print(TITLE_EVEN)
    run_game(get_num_and_answer, NUM_OF_REPEAT, EVEN_INSTR)
