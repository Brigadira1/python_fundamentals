def test():
    try:
        print("In the function")
        return 5
    finally:
        print("In the finally block")


print(test())
