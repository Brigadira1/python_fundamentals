import random

element = int(input("Enter an el to be found in the list - it should be an integer value: "))
number_of_elements = 0

list = []

for i in range(1000):
    j = random.randrange(0, 1000)
    list.append(j)

list.sort()


def binary_search(el):
    left = 0
    right = 999
    while left <= right:
        mid = int((right + left) / 2)
        number_of_elements
        number_of_elements += 1
        if el == list[mid]:
            number_of_elements += 1
            return list.index(el)
        elif el < list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


index = binary_search(element)

print(f"Number of tries: {number_of_elements}")

if index == -1:
    print("No such element")
else:
    print(f"The index of {element} is: {index}")
