import random
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_EVEN, EVEN_INSTR


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_desired_numer_and_answer():
    num = random.randint(1, 100)
    answer = is_even(num)
    return num, answer


def run_even_game():
    print(NAME_GAME_EVEN)
    run_game(get_desired_numer_and_answer(), EVEN_INSTR)
