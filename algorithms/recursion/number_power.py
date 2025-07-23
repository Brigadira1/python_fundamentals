def number_power(number: int, power: int):
    if power == 0:
        return 1
    else:
        return number * number_power(number, power - 1)


print(number_power(10, 4))
