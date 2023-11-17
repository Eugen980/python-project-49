from brain_games.random_number import random_number
from brain_games.engine import run_game
from brain_games.consts import NAME_GAME_PROGRESSION, PROGRESS_INSTR


def get_sequence(len_sequence):
    seq = []
    step, first_num = random_number(b=5), random_number()
    for _ in range(first_num, first_num + len_sequence):
        seq.append(str(_ * step))
    return seq


def get_sequence_and_answer():
    len_sequence = 10
    random_num = random_number(a=0, b=len_sequence - 1)
    sequence = get_sequence(len_sequence)
    answer = sequence[random_num]
    sequence[random_num] = '..'
    question = " ".join(sequence)
    return question, answer


def run_progress_game():
    print(NAME_GAME_PROGRESSION)
    run_game(get_sequence_and_answer, PROGRESS_INSTR)
