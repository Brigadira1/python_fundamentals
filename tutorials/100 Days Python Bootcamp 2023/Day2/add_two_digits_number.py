number = input("Enter a two digits number: ")
if len(number) != 2:
    print("Enter EXACTLY 2 digits number!")
    exit(1)

print(f"The sum of the digits of your number is {number[0]} + {number[1]} = {int(number[0]) + int(number[1])}")
