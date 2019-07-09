class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @length.setter
    def length(self, value):
        ratio = value / self.length
        self.x = ratio * self.x
        self.y = ratio * self.y


v = Vector(3, 4)
print(v.x, v.y, v.length)
# v.set_length(10)
v.length = 10
print(v.x, v.y, v.length)
v.x = 2
print(v.x, v.y, v.length)