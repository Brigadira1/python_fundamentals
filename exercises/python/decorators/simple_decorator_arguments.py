def display_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Decorating {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper


@display_decorator
def display(name: str, age: int):
    print(f"Name is {name} and age is {age}")


display("Iavor", 46)
