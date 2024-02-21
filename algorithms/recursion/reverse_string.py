rev_string = input("Enter a string to be reversed: ")


def reverse_string(string):
    if string == "":
        return ""
    else:
        return reverse_string(string[1:]) + string[0]


print(f"The reversed string is: {reverse_string(rev_string)}")
