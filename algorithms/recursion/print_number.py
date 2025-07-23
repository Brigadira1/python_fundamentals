def print_number(n):
    if n < 1:
        print(f"printing the number {n}")
    else:
        print_number(n - 1)
        print(n)


print_number(4)
