from random import randint

from src.utils import clear_screen


def get_sides():
    good_input = False
    while good_input == False:
        sides = input('How many sided dice? (2-99) :')
        try:
            val = int(sides)
            if val > 99 or val <= 0:
                print("Must be between 1 and 99.")
                good_input = False
            else:
                good_input = True
        except ValueError:
            try:
                val = float(sides)
                print("Input must be a number")
            except ValueError:
                print("Input must be a number")

    return sides


def roll(sides):
    return str(randint(1, int(sides))).zfill(2)


def running_screen(sides):
    print('You have chosen {} sides!'.format(str(sides)))
    print('*' * 10)
    print('*' + ' ' * 8 + '*')
    print('*' + ' ' * 8 + '*')
    print('*' + ' ' * 3 + roll(sides) + ' ' * 3 + '*')
    print('*' + ' ' * 8 + '*')
    print('*' + ' ' * 8 + '*')
    print('*' * 10)


def game_on(sides):
    run = True
    while run:
        clear_screen()
        running_screen(sides)
        go = input('Any key to roll again. (E to exit)')
        if go.upper() == 'E':
            run = False


def play():
    run = False
    clear_screen()
    sides = get_sides()
    game_on(sides)
