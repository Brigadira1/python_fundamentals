from typing import Iterable


class Range:
    def __init__(self, end: int):
        self.end = end

    def __iter__(self) -> Iterable[int]:
        current = 0
        while current < self.end:
            yield current
            current += 1


def test_generator():
    for i in Range(5):
        print(f"{i} iteration of the generator...")


test_generator()
