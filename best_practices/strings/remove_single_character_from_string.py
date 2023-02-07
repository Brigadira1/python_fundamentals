"""
This is an ingenious way to remove a single character in a string knowing its occurrence index.

"""

def remove_string_character (str, index):
    return str[:index] + str[index + 1:]

str = "This is a test string, which tests the remove single character by occurrence index"

print(remove_string_character(str, 2))





