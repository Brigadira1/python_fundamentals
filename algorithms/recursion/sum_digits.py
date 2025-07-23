def sum_numbers(n: int):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_numbers(n // 10)


print(sum_numbers(55555))
