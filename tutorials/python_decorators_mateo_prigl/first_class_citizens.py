def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


plus = add
print(plus(2, 3))
print(add)
print(plus)

operations = [add, subtract]

print(operations[1](5, 3))


def greeting_message():
    print("Welcome to your new job!")
