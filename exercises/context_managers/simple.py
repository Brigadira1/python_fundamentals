class CustomCM:
    def __init__(self):
        self.i = 5

    def __enter__(self):
        print("__enter()__")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit()__")

    def stop_complaining(self):
        pass


def main():
    with CustomCM() as cm:
        print(type(cm))
        cm.stop_complaining()
        print("__middle__()")

    print("__After the context manager is over__")


if __name__ == "__main__":
    main()
