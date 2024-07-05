import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def circumference(self):
        return 2*math.pi*self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def circumference(self):
        return 2*self.side

    def __repr__(self) -> str:
        return f"Square(side={self.side})"


if __name__ == "__main__":
    circle = Circle(10)
    square = Square(5)

    for shape in [circle, square]:
        print(type(shape))
        print(shape)
