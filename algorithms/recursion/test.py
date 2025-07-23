def factorial(n: int):
    if n == 0:
        return 1
    else:
        print(f"In this iteration n is equal to {n}")
        return n * factorial(n - 1)


print(factorial(10))
