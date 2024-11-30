import time
from threading import Thread


def print_epoch(thread_name: str, delay: int) -> None:
    counter = 0
    while counter < 5:
        print(f"The current time is displayed by {thread_name} and is: {time.time()}")
        time.sleep(delay)
        counter += 1


t1 = Thread(target=print_epoch, args=("Thread-1", 1))
t2 = Thread(target=print_epoch, args=("Thread-2", 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads finished execution.")
