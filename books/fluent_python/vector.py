import math


class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __mul__(self, scalar: int):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool((self.x or self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


vec1 = Vector(1, 2)
vec2 = Vector(4, 3)
vec3 = Vector(0, 0)

sum_vectors = vec1 + vec2
scalar_mult = sum_vectors * 5
abs_ = abs(vec2)
bool_ = bool(vec1)

print(bool(Vector(0, 0)))
print(abs_)
print(sum_vectors)
print(scalar_mult)
