# First method - transform the string to a list, update the character and return the list back to string

string1 = "This is a string in which we would like to replace a character!"
string_as_list = list(string1)
string_as_list[2] = 'A'
string2 = "".join(string_as_list)
print(string2)


# Second method - using string slicing

new_string = string1[0:2] + 'A' + string1[3:]
print(new_string)