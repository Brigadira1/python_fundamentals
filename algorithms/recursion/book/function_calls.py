def a():
    print("a() was called")
    b()
    print("a() returns")

def b():
    print("b() was called")
    c()
    print("b() returns")

def c():
    print("c() was called")
    print("c() returns")

if __name__ == '__main__':
    a()
