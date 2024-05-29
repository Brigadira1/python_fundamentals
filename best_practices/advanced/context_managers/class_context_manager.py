import os

# TEST



class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exec_type, exec_val, traceback):
        self.file.close()


with OpenFile("delmeeeeeeeeeeeeee.txt", "w") as f:
    f.write("This is a test of context manager in Python!!!")

print(os.getcwd())
print(f.closed)
