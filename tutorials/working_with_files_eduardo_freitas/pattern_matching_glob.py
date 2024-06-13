from pathlib import Path


def match(fld, pattern):
    pattern_list = Path(fld).glob(pattern)
    for fn in pattern_list:
        print(fn)


match("./files", "**/*.csv")
