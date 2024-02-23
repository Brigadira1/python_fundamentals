import random

words_list: tuple[str] = ("abbreviation", "celebration", "concentrate", "reproductive")
current_word: str = random.choice(words_list)
print(*current_word)
guess_list: list = [0] * len(current_word)
number_of_lives = 7


def is_word_guessed(g_list: list) -> bool:
    if 0 in g_list:
        return False
    else:
        return True


def print_word() -> None:
    for let in guess_list:
        if let == 0:
            print("_", end=" ")
        else:
            print(let, end=" ")


def main():
    while True:
        letter = input("Guess one letter: ")
        if len(letter) != 1:
            print("Please, enter exactly one letter!")
            continue

        guess_success = False
        for index, current_letter in enumerate(current_word):
            if current_letter == letter:
                guess_list[index] = letter
                guess_success = True

        if not guess_success:
            number_of_lives -= 1
            print(f"There is no {letter} in the word. You have {number_of_lives} left!")
            if number_of_lives == 0:
                print("You lost and couldn't guess the word! Better luck next time!")
                break
            continue

        elif is_word_guessed(guess_list):
            print(f"Congratulations!! You guessed the word '{current_word}'")
            break
        else:
            print(f"You've correctly guessed the letter '{letter}'")
            print_word()


if __name__ == "__main__":
    main()
