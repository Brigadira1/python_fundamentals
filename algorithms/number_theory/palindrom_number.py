def reversed_number(n: int) -> int:
    m = n
    reversed = 0
    while (m != 0):
        last_digit = m % 10
        reversed = reversed * 10 + last_digit
        m = m // 10

    return reversed


if __name__ == '__main__':
    number = int(input("Enter a number to be reversed: "))
    print(f"The reversed number of {number} is {reversed_number(number)}")
