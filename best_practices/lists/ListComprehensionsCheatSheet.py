# Using list comprehension to put all elements of list in a new list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_nums = [n for n in nums]

print(l_nums)

# Using list comprehension to create a new list with all numbers multiplied by themselves
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_nums = [n*n for n in nums]

print(l_nums)

# Using list comprehension to put only even numbers in a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_nums = [n for n in nums if n%2 == 0]

print(l_nums)

# Using list comprehension to create tuple. Simulates two nested for loops
list = [(letter, number) for letter in 'abcd' for number in range(4)]

print(list)

