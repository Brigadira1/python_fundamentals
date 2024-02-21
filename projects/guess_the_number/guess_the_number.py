import random


def play():

    n = ""
    while True:
        n = input("Enter a number greater or equal to zero or press 'Q' to quit the game: ")
        if n.lower() == "q":
            exit()

        if not is_a_number(n):
            print(f"{n} is not a number!!")
            continue

        n = string_to_int(n)
        if n < 0:
            print(f"{n} should be greater or equal to zero!")
            continue
        break

    num_to_guess = random.randint(0, n)

    while True:
        user_input = input(f"Now try to guess a number between 0 and {n}: ")
        if not is_a_number(user_input):
            print(f"{n} is not a number!!")
            continue
        user_input = string_to_int(user_input)

        if not is_in_range(user_input, 0, n):
            print(f"{user_input} is not in the range between 0 and {n}!")
            continue

        if num_to_guess == user_input:
            print(f"Congratulations!!! You've guessed the number!!!! It was really {num_to_guess}")
            break

        if num_to_guess < user_input:
            print(f"The number that you've guessed {user_input} is higher than my number. Guess again!")
            continue

        if num_to_guess > user_input:
            print(f"The number that you've guessed {user_input} is lower than my number. Guess again!")
            continue


def is_a_number(n):
    try:
        n = int(n)
    except ValueError:
        return False
    return True


def is_in_range(n, minimum, maximum):
    if minimum <= n <= maximum:
        return True
    return False


def string_to_int(n):
    if is_a_number(n):
        return int(n)
    else:
        return -1


if __name__ == "__main__":
    play()










