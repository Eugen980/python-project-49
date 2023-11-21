from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_EVEN, EVEN_INSTR


def is_even(number):
    result = 'yes' if number % 2 == 0 else 'no'
    return result


def get_even_or_odd_numer_and_answer():
    num = get_random_number(b=100)
    answer = is_even(num)
    return num, answer


def run_even_game():
    run_game(get_even_or_odd_numer_and_answer, NAME_GAME_EVEN, EVEN_INSTR)
