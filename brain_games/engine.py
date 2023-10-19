import prompt


def engine(game):  # Так и не понял про передачу конкретного значения вместо модуля
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.MANUAL)
    right_answer = True
    for i in range(3):
        answer = (game.init_game())
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer;(. ", end=" ")
            print(f"Correct answer '{answer}'")
            print(f"Let's try again, {name}!")
            right_answer = False
            break
    if right_answer is True:
        print(f'Congratulations, {name}!')
