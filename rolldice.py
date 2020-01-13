from os import system, name
from random import randint

def clear_screen():
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and or linux
    else:
        _ = system('clear')

def get_sides():
    sides = input('How many sided dice? (2-99) :') 
    if sides.isnumeric:
        if sides > 99:
            print('Number of sides must be less than 99')
            
    return sides

def roll(sides):
    return str(randint(1, int(sides))).zfill(2)

def running_screen(sides):
    print('You have chosen {} sides!'.format(str(sides)))
    print('*'*10)
    print('*'+ ' '*8 + '*')
    print('*'+ ' '*8 + '*')
    print('*'+ ' '*3 + roll(sides) + ' '*3 + '*')
    print('*'+ ' '*8 + '*')
    print('*'+ ' '*8 + '*')
    print('*'*10)

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
