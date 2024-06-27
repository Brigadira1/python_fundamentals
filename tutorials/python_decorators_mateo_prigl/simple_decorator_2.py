from typing import Callable


def greetings_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print("Hello Dear colleagues,\n")
        func()
        print("\nBest Regards,\nIavor Stoimenov")

    return wrapper


@greetings_decorator
def greetings_message():
    print("Welcome to SAP Labs Bulgaria!")


greetings_message()
print(greetings_message.__closure__)
print(greetings_message.__closure__[0])
print(greetings_message.__closure__[0].cell_contents)
