from pathlib import Path

names = ["Iavor", "Margarita", "Emiliana", "Daniel", "Yavora", "Momchil"]
names_file = Path(__file__).parent / "character.txt"


def write_file():
    with open(names_file, "w+") as file:
        for name in names:
            file.write(name + "\n")

        # file.seek(0)
        # print(file.readlines())
        # file.seek(0)
        # print(file.readline())


def read_file():
    with open(names_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.rstrip())


def read_file2():
    with open(names_file, "r") as file:
        for row in file:
            yield row.rstrip()


def main():
    write_file()
    # read_file()
    for row in read_file2():
        print(row)


if __name__ == "__main__":
    main()
