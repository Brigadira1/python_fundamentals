class display_class_decorator:
    def __init__(self, decorated_function):
        self.decorated_function = decorated_function

    def __call__(self, *args, **kwargs):
        print(f"Class decorator for function {self.decorated_function.__name__}")
        return self.decorated_function(*args, **kwargs)


@display_class_decorator
def display(name: str, age: int):
    print(f"The name is {name} and age is {age}")


display("Iavor", 46)
