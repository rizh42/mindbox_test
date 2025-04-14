import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) == 0


def calculate_area(shape) -> float:
    if isinstance(shape, Shape):
        return shape.area()
    elif isinstance(shape, (int, float)):
        return Circle(shape).area()
    elif isinstance(shape, tuple) and len(shape) == 3:
        return Triangle(*shape).area()
    else:
        raise ValueError("Invalid shape specification")
    

circle = Circle(5)
print(f"Circle area: {circle.area()}")

triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area()}")
print(f"Is right-angled: {triangle.is_right_angled()}")

print(f"Circle area via calculate_area: {calculate_area(5)}")
print(f"Triangle area via calculate_area: {calculate_area((3, 4, 5))}")