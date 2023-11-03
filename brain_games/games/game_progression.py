from random import randint
from brain_games.engine import run_game
from brain_games.games.consts import TITLE_PROGRESSION, PROGRESS_INSTR


def get_sequence_and_answer():
    sequence = []
    step = randint(1, 5)
    len_seq = 10
    first_element = randint(1, 30)
    random_element = randint(0, len_seq - 1)
    for i in range(first_element, first_element + len_seq):
        sequence.append(str(i * step))
    answer = sequence[random_element]
    sequence[random_element] = '..'
    sequence = " ".join(sequence)
    return sequence, answer


def run_progress_game():
    run_game(get_sequence_and_answer, TITLE_PROGRESSION, PROGRESS_INSTR)
