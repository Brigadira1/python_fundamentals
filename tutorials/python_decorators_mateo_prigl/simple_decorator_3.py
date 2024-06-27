from typing import Callable
from functools import wraps


def greetings_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello Dear colleagues,\n")
        func(*args, **kwargs)
        print("\nBest Regards,\nIavor Stoimenov")

    return wrapper


@greetings_decorator
def greetings_message(x):
    """A simple function that greets a new colleague"""
    print(f"Welcome to SAP Labs Bulgaria! Today is your {x} day at work.")


greetings_message(1)
print()
print(greetings_message.__name__)
print(greetings_message.__doc__)
print()
print(greetings_message.__closure__)
print(greetings_message.__closure__[0])
print(greetings_message.__closure__[0].cell_contents)
