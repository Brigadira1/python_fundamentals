"""This function takes the first and the last characters in a String and interchange their positions - the first
    becomse the last and vise versa - the last becomes the first. The rest of the String is not changed.
"""


def front_back(string):

    # How to access the first character of a string - first_char = str[:1]
    # The best way to access the first character of a string - first_char = str[0]
    # How to access the last character of a string - last_char = str[-1: len(str)] or str[len(str) - 1]
    # The best way to access the last el of a string is str[-1]

    new_string = string[-1] + string[1:len(string) -1] + string[0]
    return new_string


string = "This is a test string to test the program"
print(front_back(string))


