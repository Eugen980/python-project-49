import prompt
from brain_games.consts import WRONG_ANSWER


def run_game(get_question_and_answer, num_of_round, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}\n{instruction}')
    for _ in range(num_of_round):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question} Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' {WRONG_ANSWER} '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
