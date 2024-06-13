import os, fnmatch


def match(fld: str, pattern: str):
    [print(fn) for fn in os.listdir(fld) if (fnmatch.fnmatch(fn, pattern))]


match("./files", "*.csv")
