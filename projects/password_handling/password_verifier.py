import string


class PasswordVerifier:
    def __init__(self, password):
        self.password = password
        self.__digits = None
        self.__capitals = None
        self.__specials = None
        self.__lowers = None

    def _is_digit(self):
        if not self.password:
            return False

        self.digits = [1 if c in string.digits else 0 for c in self.password]

        return any(self.digits)

    def _is_capital(self):
        if not self.password:
            return False

        self.capitals = [1 if c in string.ascii_uppercase else 0 for c in self.password]

        return any(self.capitals)

    def _is_special(self):
        if not self.password:
            return False

        self.specials = [1 if c in string.punctuation else 0 for c in self.password]

        return any(self.specials)

    def _is_lower(self):
        if not self.password:
            return False

        self.lowers = [1 if c in string.ascii_lowercase else 0 for c in self.password]

        return any(self.lowers)

    def _is_commonly_used(self):

        with open("10-million-password-list-top-1000000.txt", 'r') as file:
            common = file.read().splitlines()

        if self.password in common:
            return True
        else:
            return False

    def validate_password(self):
        if self._is_lower() \
                and self._is_special() \
                and self._is_digit() \
                and self._is_capital() \
                and not self._is_commonly_used() \
                and 5 < len(self.password) < 30:
            print("You password is a valid password, containing small letters, capital letters, special symbols. "
                  "It is also contains more than 5 symbols and less than 30 symbols. ")

        else:
            print("You password is invalid!!!")


    def print_all(self):

        print(self.lowers)
        print(self.digits)
        print(self.specials)
        print(self.capitals)


if __name__ == "__main__":
    password = "As!3555555lkerfgasaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    password_verifier = PasswordVerifier(password)
    (password_verifier.validate_password())
    # password_verifier.print_all()
