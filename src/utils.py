from os import name, system


def clear_screen():
    # for windows
    # print(name)
    if name == 'nt':
        _ = system('cls')

    # for mac and or linux
    else:
        _ = system('clear')


def good_integer_between(a: int, b: int, u_input) -> bool:
    try:
        val = int(u_input)
        if val > b or val < a:
            print("Must be between {} and {}.".format(str(a), str(b)))
            return False
        else:
            return True
    except ValueError:
        try:
            val = float(u_input)
            print("Input must be a whole number")
            return False
        except ValueError:
            print("Input must be a whole number")
            return False
