from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import EVEN_INSTR


def is_even(number):
    return number % 2 == 0


def get_even_or_odd_numer_and_answer():
    num = get_random_number(end=100)
    answer = 'yes' if is_even(num) else 'no'
    return num, answer


def run_even_game():
    run_game(get_even_or_odd_numer_and_answer, EVEN_INSTR)
