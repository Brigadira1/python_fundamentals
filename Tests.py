import os
import sys


def poorly_formatted_function(x, y):
    z = x + y
    if z == 5:
        print("The sum is 5")
    else:
        print("The sum is not 5")

    unused_variable = 10

    return z


result = poorly_formatted_function(2, 3)
print(f"The result is: {result}")

# Unused import
import datetime
