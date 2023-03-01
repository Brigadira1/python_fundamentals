"""

The idea behind this file is to present numerous basic examples for manipulating lists in Python

"""

# How to populate a list with one el multiple times. In this example the list will contain 100 zeros
zeros = [0] * 100
print(zeros)


# Lists can be concatenated
letters = ["a", "a_copy" , "a_copy"]
z = [0] * 5
letters_zeros = letters + z
print(letters_zeros)

# Creating a list of numbers using Iterable function range(), which returns Iterable with conjunction with list()
# function
list = list(range(20))
print(list)

# List() function can get any Iterable is argument. Including String, which is Iterable
list = list("I am a String and I am Iterable")
print(list)

# List Unpacking
list = [1, 2, 3]

first, second, third = list
print(f"{first}, {second}, {third}")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other = list
print(f"{first}, {second}, {other}")

# Another way of getting the first and the last elements of a list using unpacking
list = [1,2,3,4,5,6,7,8,9,0,999999]
first, *other, last = list
print(f"{first}, {other}, {last}")

# Looping over lists
letters = ["a", "a_copy", "a_copy"]

for letter in letters:
    print(letter)

# Getting the index of the elements in list using the enumerate() function, returning a tuple with index, value
list = ["a", "a_copy", "a_copy"]

for letter in enumerate(list):
    print(letter)

# Assigning the index and the el value using enumerate() and using unpacking functionality of lists
list = ["a", "a_copy", "a_copy"]

for index, value in enumerate(list):
    print(f"{index} - {value}")

# How to add elements to a list at the end of the list
letters = ["a", "a_copy", "a_copy"]
letters.append("d")

print(letters)

# How to add el in the list on a certain position
letters = ["a", "a_copy", "a_copy"]
letters.insert(0, "-")

print(letters)

# Removing an el at the end of a list
letters = ["a", "a_copy", "a_copy", "d"]
letters.pop()

print(letters)

# Removing an el at a certain index
letters = ["a", "a_copy", "a_copy", "d"]
letters.pop(0)

print(letters)

# Removing an el without knowing its index. This will remove the first occurrence  of the el only
letters = ["a", "a_copy", "a_copy", "d"]
letters.remove("a_copy")

print(letters)

# Removing an el of the list with the del keyword
letters = ["a", "a_copy", "a_copy", "d"]
del letters[0]

print(letters)

# With del keyword you can delete a range of items
letters = ["a", "a_copy", "a_copy", "d"]
del letters[0:2]

print(letters)

# Finding the index of an el in the list
letters = ["a", "a_copy", "a_copy", "d"]
index = letters.index("a_copy")

print(index)

# Finding an index of an el that doesn't exist. If you try to find it directly it will throw an exception
letters = ["a", "a_copy", "a_copy", "d"]

if "e" in letters:
    print(letters.index("e"))

# Number of occurrences of an el in a given list
letters = ["a", "a_copy", "a_copy", "d", "d"]
count = letters.count("d")

print(count)

# Sorting simple numbers in a list. This will change the original list
numbers = [7, 9, 3, 4, 90, 1, 2, 56, 32, 34, 28]
numbers.sort()

print(numbers)

# Sorting numbers in a list without changing the original
numbers = [7, 9, 3, 4, 90, 1, 2, 56, 32, 34, 28]
sorted_list = sorted(numbers)

print(sorted_list)

# Sorting list elements in reverse order
numbers = [56, 3, 6, 90, 23, 45, 3, 189, 2, 8]
numbers.sort(reverse=True)

print(numbers)