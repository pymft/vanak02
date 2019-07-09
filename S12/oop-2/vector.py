import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(self.x ** 2 + self.y ** 2)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y

        return Vector(x_new, y_new)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        # return self + (-other)
        return Vector(self.x - other.x, self.y - other.y)



def vector_adder(a: Vector, b: Vector) -> Vector:
    x = a.x + b.x
    y = a.y + b.y
    return Vector(x, y)


def length_of_vector(vec: Vector) -> float:
    return math.sqrt(vec.x ** 2 + vec.y ** 2)


v1 = Vector(3, 4)
v2 = Vector(9, 1)
v3 = v1 + v2
print(v3.get_length())
print(v3.length)

