import random

game_set = ("scissors", "stone", "paper")

def play():
    while True:
        computer_choice = random.choice(game_set)
        user_input = input("Enter your choice ('scissors', 'stone' or 'paper') or press Q for exiting the game: ")
        if user_input.lower() == "q":
            exit()

        if user_input not in game_set:
            print("Your input is invalid! Try entering it again")
            continue

        if user_input == game_set[0]:
            if computer_choice == game_set[0]:
                print(f"Your choice is {user_input}. Mine as well! It is a tie!")
                continue
            elif computer_choice == game_set[1]:
                print(f"Your choice is {user_input} and mine is {computer_choice}. Sorry, brother I win !!!")
                continue

            elif computer_choice == game_set[2]:
                print(f"Your choice is {user_input}. My choice was {computer_choice}. You win, brother!")
                continue

        elif user_input == game_set[1]:
            if computer_choice == game_set[0]:
                print(f"Your choice is {user_input}. Mine is {computer_choice}. You win !!!")
                continue
            elif computer_choice == game_set[1]:
                print(f"Your choice is {user_input}. Mine as well! It is a tie!")
                continue

            elif computer_choice == game_set[2]:
                print(f"Your choice is {user_input}. My choice was {computer_choice}. I win, brother!")
                continue

        else:
            if computer_choice == game_set[0]:
                print(f"Your choice is {user_input}. My choice was {computer_choice}. I win, brother!")
                continue
            elif computer_choice == game_set[1]:
                print(f"Your choice is {user_input}. My choice was {computer_choice}. You win, brother!")
                continue

            elif computer_choice == game_set[2]:
                print(f"Your choice is {user_input}. Mine as well! It is a tie!")
                continue


if __name__ == "__main__":
    play()
