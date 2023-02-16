list = ["a", "a_copy", "a_copy", "d"] * 8
print(list)

# Here is an example how we can produce a new list with every second element from the first
every_second_element_list = list[::2]

print(every_second_element_list)

# The same pattern can be used to iterate over every n-th element of the list

every_fourth_element_list = list[::4]

print(every_fourth_element_list)