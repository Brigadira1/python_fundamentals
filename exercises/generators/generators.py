def simple_generator():
    yield "I "
    yield "love "
    yield "programming! "
    yield 2024


# It is necessary to store the Generator in a variable to be used in each iteration.
# If you simply pass simple_generator() to each next() call, it created a new Generator object in memory and always prints "I"
gen = simple_generator()
item1 = next(gen)
print(item1)
item2 = next(gen)
print(item2)
item3 = next(gen)
print(item3)
item4 = next(gen)
print(item4)

# Causes StopIteration exception
# item5 = next(gen)
# print(item5)

# With a for loop you can directly invoke the genrator function.
for item in simple_generator():
    print(item)

# The generator is already exausted so this won't print anything
for item in gen:
    print(item)


class Range:
    def __init__(self, stop: int):
        self.stop = stop
        self.index = 0

    def __iter__(self) -> Itartor[int]:

        return self
