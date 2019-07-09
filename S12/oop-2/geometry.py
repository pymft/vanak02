class Rectangle:
    """

    Example
    -------
    >>> rect = Rectangle(10.0, 4.0)
    >>> rect.area()
    40.0
    >>> rect.perimeter()
    28.0
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2


class Square(Rectangle):
    """

    Example
    -------
    >>> square = Square(10.0)
    >>> square.area()
    100.0
    >>> square.perimeter()
    40.0
    """

    def __init__(self, side: float):
        self.width = side
        self.height = side





if __name__ == '__main__':
    import doctest

    doctest.testmod()
