from os import name, system


def clear_screen():
    # for windows
    #print(name)
    if name == 'nt':
        _ = system('cls')

    # for mac and or linux
    else:
        _ = system('clear')