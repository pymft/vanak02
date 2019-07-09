class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y

        return Vector(x_new, y_new)

    def __sub__(self, other):
        pass

    def __neg__(self):
        pass


v1 = Vector(3, 4)
v2 = Vector(10, 1)
v3 = v1 + v2 + v1 + v2 + v2
print(v3.x, v3.y)
