"""

This program checks whether all elements in a list (the shorter one) are contained in the longer list.
Pay attention to the fact that the elements from the first list can be on arbitrary place in the second.
Another algorithm is needed if the sequence of elements from the first list (the shorter one) is present
in the second list.

"""


def check_numbers_in_lists (a, b):
    for item in a:
        if item not in b:
            return False
    return True

a = [2, 2, 3]
b = [2, 3, 4, 5, 9]

if (len(a) <= len(b)):
    print(check_numbers_in_lists(a, b))
else:
    print(check_numbers_in_lists(b, a))
