def is_palyndrom(string):
    if len(string) == 0 or len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return is_palyndrom(string[1:-1])
    else:
        return False


pal_string = input("Enter a string to check whether it is palyndrom or not: ")
a = is_palyndrom(pal_string)

if a is True:
    print(f"The string that you've entered '{pal_string}' is a palyndrom")
else:
    print(f"The string that you've entered '{pal_string}' IS NOT a palyndrom")
