from enum import Enum, auto


class Colors(Enum):
    RED = auto()
    GREEN = auto()
    WHITE = auto()
    YELLOW = auto()


print(type(Colors.RED))
print(type(Colors.RED.name))
print(type(Colors.RED.value))
print(Colors.RED.name)
print(Colors.RED.value)

# Enums are immutable:

"""This will not work:"""
# Colors.RED = 5


"""This will not work as well:"""
Colors.BROWN = 19
