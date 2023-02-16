""" This function receive two numbers. check which of the numbers are even
    and puts the im a list, which is returned.
"""


def even_numbers(x, y):
    a = []
    for number in range(x, y + 1):
        if number % 2 == 0:
            a.append(number)
    return a


x = input("Please, enter a number: ")
y = input("Please enter a second number:")

a = even_numbers(int(x), int(y))

print(f"All the even number between {x} and {y} are: " + str(a))
print(f"Between {x} and {y} there are " + str(len(a)) + " even numbers")
