"""
This program uses the random.sample() function to generate a list with random elements

"""

import random

list = random.sample(range(0, 100), 100)

print(list)

list.sort()

print(list)