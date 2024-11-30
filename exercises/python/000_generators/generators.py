from typing import Iterator


def simple_generator():
    yield "I "
    yield "love "
    yield "programming! "
    yield 2024


# It is necessary to store the Generator in a variable to be used in each iteration.
# If you simply pass simple_generator() to each next() call, it created a new Generator object in memory and always prints "I"
generator = simple_generator()
item1 = next(generator)
print(item1)

item2 = next(generator)
print(item2)
item3 = next(generator)
print(item3)
item4 = next(generator)
print(item4)

# Causes StopIteration exception
# item5 = next(gen)
# print(item5)

# With a for loop you can directly invoke the genrator function.
for item in simple_generator():
    print(item)

# The generator is already exausted so this won't print anything
for item in generator:
    print(item)


class RangeIter:
    def __init__(self, stop: int):
        self.stop = stop
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.stop:
            return self.index
        else:
            raise StopIteration


for i in RangeIter(5):
    print(f"This is the Iterator printing: {i=}")


class RangeGen:
    def __init__(self, stop):
        self.stop = stop
        self.current = 0

    def __iter__(self) -> Iterator[int]:
        while self.current < self.stop:
            yield self.current
            self.current += 1


print()

for i in RangeGen(20):
    print(f"This is the Generator printing: {i=}")
