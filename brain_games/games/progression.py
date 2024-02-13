from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import PROGRESS_INSTR, LENGHT_SEQUENCE


def get_progression_and_missed_num():
    random_num = get_random_number(start=0, end=LENGHT_SEQUENCE - 1)
    step, start = get_random_number(end=5), get_random_number()
    progression = list(range(start, start + step * LENGHT_SEQUENCE, step))
    missed_num = str(progression[random_num])
    progression[random_num] = '..'
    progression = ' '.join(map(str, progression))
    return progression, missed_num


def run_progression_game():
    run_game(get_progression_and_missed_num, PROGRESS_INSTR)
