import logging
from functools import wraps
from typing import Callable

logging.basicConfig(level=logging.INFO)


def log_funciton_call(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Calling function {func.__name__} with arguments {args} and key word arguments {kwargs}"
        )
        return func(*args, **kwargs)

    return wrapper


@log_funciton_call
def add(a, b):
    return a + b


print(add(5, 3))
print(add(203948, 2039482304823094))
