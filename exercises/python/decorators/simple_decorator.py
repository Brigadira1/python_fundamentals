def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function()

    return wrapper_function


# @decorator_function
def display():
    print(f"I am the original {display.__name__}")


decorated_function = decorator_function(display)
decorated_function()
# display()
