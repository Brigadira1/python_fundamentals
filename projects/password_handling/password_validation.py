def is_password_valid(passwd):
    if 5 < len(password) < 20:
        digit = False
        capital_letter = False
        small_letter = False
        special_symbol = False

        for char in password:
            if char.isdigit():
                digit = True
            if char.islower():
                small_letter = True
            if char.isupper():
                capital_letter = True
            if not char.isalnum():
                special_symbol = True

        return digit and capital_letter and small_letter and special_symbol

    return False


def is_password_valid2(passwd):
    pass


password = "Ab1!a634567498567495679485768945768945769485769485679485769456459867"
print(is_password_valid(password))
