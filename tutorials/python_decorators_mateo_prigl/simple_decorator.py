from typing import Callable


def greetings_message():
    print("Welcome to SAP Labs Bulgaria!")


def greeting_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print("Hello Dear colleagues,\n")
        func()
        print("\nBest Regards,\nIavor Stoimenov")

    return wrapper


greetings_message = greeting_decorator(greetings_message)
greetings_message()
