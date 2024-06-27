from functools import wraps


def company_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("SAP AG, Dietmar Hopp Strasse 1")

    return wrapper


def email_decorator(fromWho):
    def _email_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Dear interns,\n")
            func(*args, **kwargs)
            print(f"\nBest Regards,\nYour new {fromWho}")

        return wrapper

    return _email_decorator


@company_info
@email_decorator(fromWho="Boss")
def greetings_message(x):
    """This is a simple greetings function to greet new interims"""
    print(f"Welcome, on your new {x}!")


greetings_message("job")
