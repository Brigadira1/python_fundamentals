"""

This program tests whether a list is contained in another list.
Please, be aware that the elements in the first (shorter list) should be contained in the second (longer list)
exactly in the same sequence as they are in the first - shorter list.

"""

def list_contained (a, b):
    pass

a = [1, 2, 3, 4]
b = [1, 2, 4, 5, 9, 15, 1, 2, 3, 5, 1, 2, 3, 4, 1, 2, 3, 9]

if (len(a) <= len(b)):
    print(list_contained(a, b))
else:
    print(list_contained(b, a))
