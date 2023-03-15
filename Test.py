def bubble_sort(list):

    for i in range(0, len(list)):
        sorted = True
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j+1]
                sorted = False

        if sorted:
            return list

    return list

# list=[1,2,8,4,5,6,7,2,3,4,5,99, 100, 45]
# print(bubble_sort(list))


def insertion_sort(list):
    for i in range(1, len(list)):
        j = i

        while list[j - 1] > list[j] and j > 0:
            list[j], list[j-1] = list[j - 1], list[j]
            j -= 1

    return list



list=[98, 34, 23, 29, 4, 5, 46, 768, 0,]
print(insertion_sort(list))