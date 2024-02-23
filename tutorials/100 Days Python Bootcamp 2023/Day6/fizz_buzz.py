for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"The {num} divides by both 3 and 5")

    elif num % 3 == 0:
        print(f"The {num} divides by 3")

    elif num % 5 == 0:
        print(f"The {num} divides by 5")
