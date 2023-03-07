n = int(input("Enter a positive number: "))

def sum(number):

    if number == 0:
        return 0

    return number + sum(number-1)

print(f"The sum is: {sum(n)}")
