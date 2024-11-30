from collections import namedtuple
from typing import NamedTuple

Color = namedtuple("Color", ["red", "blue", "white"])
color = Color(123, 345, 456)
print(f"Color is: {color.red}")
print(f"Color is: {color[1]}")


class Color1(NamedTuple):
    red: int
    blue: int
    white: int


color1 = Color1(999, 1000, 1001)
print(f"The name of the color from the NamedTuple is: {color1.red}")
print(f"The name of the color from the NamedTuple is: {color1[2]}")
