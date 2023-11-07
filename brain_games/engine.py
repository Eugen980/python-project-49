import prompt


def run_game(game, repeat, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}\n{instruction}')
    for i in range(repeat):
        question, answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer;(. ", end=" ")
            print(f"Correct answer '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
