import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length(self, norm=2) -> float:
        return (self.x ** norm + self.y ** norm) ** (1/ norm)

    def __repr__(self):
        return f"VECTOR {self.x}, {self.y}"


v1 = Vector(3, 4)

print(v1.get_length(norm=1))

v1.x = 10

print(v1.get_length(norm=1))
