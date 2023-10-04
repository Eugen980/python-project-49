import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.MANUAL)
    count = 0
    right_answer = True
    while count < 3:
        answer = (game.init_game())
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer;(. ",end =" ")
            print(f"Correct answer '{answer}'")
            print(f"Let's try again, {name}!")
            right_answer = False
            count = 3
    if right_answer is True:
        print(f'Congratulations, {name}!')
