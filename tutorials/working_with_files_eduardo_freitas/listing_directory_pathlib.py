from pathlib import Path


def list_dir(fld):
    [print(fn.name) for fn in Path(fld).iterdir()]


list_dir("./files")
