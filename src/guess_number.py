from utils import clear_screen, good_integer_between
from random import randint


def get_random_number(a: int, b: int) -> int:
    return randint(a, b)


def guess_the_number(num_to_guess):
    """

    if correct - congrats
    if not check if already guessed - Already guessed - respond higher or lower
    if not add to guess list respond higher or lower
    """
    correct = False
    answer = num_to_guess
    guesses = set()
    while not correct:
        guess = input("Guess a number between 0 and 99: (e to exit)")
        if guess.upper() == 'E':
            print("Quitter")
            correct = True
            break

        if good_integer_between(0, 99, guess):
            if int(guess) == answer:
                print('You guessed correctly wih {}!'.format(str(guess)))
                print(guesses)
                break
            elif int(guess) > answer:
                print('Your guess of {} is too high.'.format(str(guess)))
                guesses.add(int(guess))
            elif int(guess) < answer:
                print('Your guess of {} is too low.'.format(str(guess)))
                guesses.add(int(guess))
    pass


def play():
    clear_screen()
    num_to_guess = get_random_number(0, 99)
    guess_the_number(num_to_guess)
