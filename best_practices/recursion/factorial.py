number = int(input("Please, enter a number >=0 to calculate the factorial of: "))
if number < 0:
    print("The number should be positive!")
    exit()

def factorial(num):
    if num == 0:
        return 1

    else:
        return num*factorial(num - 1)

print(f"Factorial of {number} is: {factorial(number)}")
