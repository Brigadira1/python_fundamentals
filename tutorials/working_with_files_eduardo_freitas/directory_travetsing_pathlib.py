from pathlib import Path


def traverse_dir(folder):
    for root, dirs, files in Path(folder).walk():
        # print(root, dirs, files, sep="\n")
        # print(root, dirs, files, sep="\n")
        print(root)
        print(dirs)
        print(files)


traverse_dir("./files")
