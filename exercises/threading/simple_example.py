import threading
import time


def f1():
    for i in range(10):
        time.sleep(0.01)
        print("ONE")


def f2():
    for i in range(10):
        time.sleep(0.03)
        print("TWO")


def f3():
    for i in range(10):
        time.sleep(0.02)
        print("THREE")


# f1()
# f2()
# f3()
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t3 = threading.Thread(target=f3)
t1.start()
t2.start()
t3.start()
# t1.join()
# t2.join()
# t3.join()
# t1 = threading.Thread(target)
