class Rectangle:
    def __init__(self, width: float, height: float):
        print("hello from Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        print("hello from Rectangle... area")
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2


class Square(Rectangle):
    def __init__(self, side: float):
        print("hello from Square")
        super().__init__(side, side)






s = Square(10)
print(s.width, s.height)

