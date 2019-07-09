class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, b):
        x_new = self.x + b.x
        y_new = self.y + b.y

        return Vector(x_new, y_new)


v1 = Vector(3, 4)
v2 = Vector(10, 1)
v3 = v1.add(v2)
v4 = v1.add(v3)
v6 = v4.add(v3)
print(v3.x, v3.y)
