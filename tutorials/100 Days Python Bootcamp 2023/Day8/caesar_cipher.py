from pyfiglet import figlet_format

print(figlet_format("Caesar Cypher", font="big"))
choices: tuple[str] = ("encode", "decode", "Q".lower())


def encode(letter: str, offset: int) -> str:
    if ord(letter) + offset > ord('z'):
        diff = ord(letter) + offset - ord('z')
        new_letter = chr(ord('a') + diff - 1)
    else:
        new_letter = chr(ord(letter) + offset)

    return new_letter


def decode(letter: str, offset: int) -> str:
    if ord(letter) - offset < ord('a'):
        diff = ord('a') - (ord(letter) - offset)
        new_letter = chr(ord('z') - diff + 1)
    else:
        new_letter = chr(ord(letter) - offset)

    return new_letter


while True:
    choice = input("Enter 'encode', 'decode' or press Q for exit: ").lower()
    if choice not in choices:
        print("Invalid input. You must enter either 'encode', 'decode' or 'Q' to quit: ")
        continue
    if choice == 'q':
        print("Quiting....")
        exit(0)
    offset: int = int(input("Enter an offset: "))
    if offset > 26:
        offset = offset % 25
    message = input(f"Enter the message to be {choice}d: ")
    if choice == choices[0]:
        encoded_message = ""
        for l in message:
            encoded_message += encode(letter=l, offset=offset)
        print(f"The encoded message is: {encoded_message}")

    else:
        decoded_message = ""
        for l in message:
            decoded_message += decode(letter=l, offset=offset)
        print(f"The decoded message is {decoded_message}")
