import random


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number beween 1 and 100.")
    computer_number = random.randrange(1, 100, 1)
    choices = ("easy", "hard")
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level not in choices:
            print(f"The only valid choices of level difficulty are 'easy' and 'hard'. You typed '{level}'")
            continue
        break
    number_of_tries = 10 if level == choices[0] else 5
    is_guessed = False
    # print(f"Computer number: {computer_number}, Level: {level}, Number of tries: {number_of_tries}")
    while number_of_tries > 0:
        print(f"You have {number_of_tries} left.")
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_number:
            print(f"You've guessed the number! It was indeed {computer_number}. You win.")
            is_guessed = True
            break
        elif user_guess > computer_number:
            print("Too high.")
            number_of_tries -= 1
            continue
        else:
            print("Tool low.")
            number_of_tries -= 1
            continue

    if not is_guessed:
        print(f"You have 0 attempts left. You lose. The number that I've guessed was {computer_number}")



if __name__ == '__main__':
    game()
