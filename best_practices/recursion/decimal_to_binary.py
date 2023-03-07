n = int(input("Enter a positive number: "))


def decimal_to_binary(number, string=""):

    if number == 0:
        return string

    reminder = number % 2
    number = int(number / 2)

    string = string + str(reminder)

    return decimal_to_binary(number) + string

print(f"The binary form of {n} is: {decimal_to_binary(n)}")

