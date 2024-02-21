def bubble_sort(items):
    """
    This version of bubble sort is the most possibly optimized one. It only goes to the part of the list with
    the already sorted elements and also returns as fast as possible if the list is already sorted
    :param items: The list that should be sorted
    :return: The sorted list of elements
    """

    for i in range(len(items)):
        sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j+1], items[j]
                sorted = False
        if sorted:
            return items

    return items


list = [8, 7, 7, 6, 5, 4, 3, 2, 1]
items = [1, 2, 3, 4, 5, 6, 7, 8, 98]
print(bubble_sort(items))
