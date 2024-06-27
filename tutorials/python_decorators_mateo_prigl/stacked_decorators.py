from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Decorator1 is invoked before {func.__name__} is invoked.")
        # return func(*args, **kwargs)
        result = func(*args, **kwargs)
        print(f"Decorator1 is invoked AFTER {func.__name__}.")

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Decorator2 is invoked before {func.__name__} is invoked.")
        # return func(*args, **kwargs)
        result = func(*args, **kwargs)
        print(f"Decorator2 is invoked AFTER {func.__name__}.")

    return wrapper


def decorator3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Decorator3 is invoked before {func.__name__} is invoked.")
        # return func(*args, **kwargs)
        result = func(*args, **kwargs)
        print(f"Decorator3 is invoked AFTER {func.__name__}.")

    return wrapper


@decorator1
@decorator2
@decorator3
def add(a, b):
    return a + b


@decorator1
@decorator2
@decorator3
def print_simple_message():
    print(
        "This is a simple message that is printed originally without decorators from the original function"
    )


# print(add(2, 3))
# print(add(10, 10))
print_simple_message()
