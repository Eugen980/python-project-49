import random
from brain_games.engine import run_game
from brain_games.consts import TITLE_PROGRESSION, PROGRESS_INSTR, NUM_OF_REPEAT


def get_sequence(len_seq):
    seq = []
    step, first_num = random.randint(1, 5), random.randint(1, 30)
    for _ in range(first_num, first_num + len_seq):
        seq.append(str(_ * step))
    return seq


def get_sequence_and_answer():
    len_seq = 10
    random_num = random.randint(0, len_seq - 1)
    sequence = get_sequence(len_seq)
    answer = sequence[random_num]
    sequence[random_num] = '..'
    question = " ".join(sequence)
    return question, answer


def run_progress_game():
    print(TITLE_PROGRESSION)
    run_game(get_sequence_and_answer, NUM_OF_REPEAT, PROGRESS_INSTR)
