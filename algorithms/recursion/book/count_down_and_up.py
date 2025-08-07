from showcallstack import showcallstack


def count_down_and_up(number: int) -> None:
    showcallstack()
    print(f"{number}")
    if number == 0:
        print("Base case was reached.")
        return
    else:
        count_down_and_up(number - 1)
        print(f"{number}")
        return

count_down_and_up(3)
