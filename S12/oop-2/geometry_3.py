

class Parallelogram:
    def __init__(self, a, b, theta):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Parallelogram):
    def __init__(self, w, h):
        super().__init__(w, h, 90)


class Diamond(Parallelogram):
    def __init__(self, a, theta):
        super().__init__(a, a, theta)


class Square1(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Square2(Diamond):
    def __init__(self, a):
        super().__init__(a, 90)
