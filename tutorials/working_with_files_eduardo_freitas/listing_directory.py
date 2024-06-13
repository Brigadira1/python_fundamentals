import os


def list_dir(fld: str):
    for fn in os.listdir(fld):
        print(fn)


list_dir("./files")
