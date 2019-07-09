import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


v1 = Vector(3, 4)

print(v1.get_length(), v1.length)

v1.x = 10

print(v1.get_length(), v1.length)
