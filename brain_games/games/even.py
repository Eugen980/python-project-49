import random
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_EVEN, EVEN_INSTR


def get_num_and_answer():
    num = random.randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    return num, answer


def run_even_game():
    print(NAME_GAME_EVEN)
    run_game(get_num_and_answer(), EVEN_INSTR)
