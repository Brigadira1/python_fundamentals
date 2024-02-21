def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while items[j - 1] > items[j] and j > 0:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1

    return items


items = [10, 11, 3, 4, 5, 2, 1,1000, 900, 3, 4, 2, 1]

print(insertion_sort(items))
