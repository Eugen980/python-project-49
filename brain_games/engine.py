import prompt


def run_game(get_question_and_answer, ground, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}\n{instruction}')
    for _ in range(ground):
        question, answer = get_question_and_answer()
        usr_answer = prompt.string(f'Question: {question} Your answer: ')
        if usr_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{usr_answer}' is wrong answer;(. Correct answer '{answer}'\n"
                f"Let's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')
