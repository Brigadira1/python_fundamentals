from pathlib import Path


def search_file(rootdir: str, filename: str):
    path = Path(rootdir)
    for cur_file in path.rglob(filename):
        yield cur_file.absolute()


if __name__ == '__main__':
    directory = input("Enter root directory: ")
    filename = input(f"Enter file to be searched for in the {directory} : ")
    for file in search_file(directory, filename):
        print(file)
    else:
        print(f"Your file {filename} was not found in {directory} ")
