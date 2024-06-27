import time
from functools import wraps
from typing import Callable


def time_function(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsedd_time = time.perf_counter() - start_time
        print(f"Funciton {func.__name__} took {elapsedd_time:.7f} seconds to run")
        return result

    return wrapper


@time_function
def complex_fun():
    time.sleep(1)


complex_fun()
