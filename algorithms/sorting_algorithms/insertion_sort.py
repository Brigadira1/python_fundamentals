def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, -1, -1):
            if items[i] < items[j-1]:
