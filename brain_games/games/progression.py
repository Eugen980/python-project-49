from brain_games.random_number import get_random_number
from brain_games.engine import run_game
from brain_games.consts import PROGRESS_INSTR


def get_sequence(len_sequence):
    sequence = []
    step, first_num = get_random_number(b=5), get_random_number()
    for _ in range(first_num, first_num + len_sequence):
        sequence.append(str(_ * step))
    return sequence


def get_sequence_and_answer():
    len_sequence = 10
    random_num = get_random_number(a=0, b=len_sequence - 1)
    sequence = get_sequence(len_sequence)
    answer = sequence[random_num]
    sequence[random_num] = '..'
    question = " ".join(sequence)
    return question, answer


def run_progression_game():
    run_game(get_sequence_and_answer, PROGRESS_INSTR)
