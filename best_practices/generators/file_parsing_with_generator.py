def example_composable():
    with open("nums.txt") as file:
        nums = (row.partition("#")[0].rstrip() for row in file)
        nums = (row for row in nums if row)
        nums = (float(c) for c in nums)
        for el in nums:
            print(el)


def main():
    example_composable()


if __name__ == "__main__":
    main()
