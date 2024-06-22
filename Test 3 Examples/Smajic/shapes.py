class Shape:
    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides: int):
        self.number_of_sides = number_of_sides

    def get_number_of_sides(self) -> int:
        return self.number_of_sides

class Rectangle(Shape):
    def __init__(self, number_of_sides: int, width: float, height: float):
        super().__init__(number_of_sides)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)
#come back to this
    def set_width(self, width: float):
        self.width = width

    def get_width(self) -> float:
        return self.width

    def set_height(self, height: float):
        self.height = height

    def get_height(self) -> float:
        return self.height

    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.width == other.get_width() and self.height == other.get_height()
        return False

    def __str__(self) -> str:
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}"

import math
class Circle(Shape):
    def __init__(self, number_of_sides: int, radius: float):
        super().__init__(number_of_sides)
        self.radius = radius
#come back to this
    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def set_radius(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def __eq__(self, other) -> bool:
        if isinstance(other, Circle):
            return self.radius == other.get_radius()
        return False

    def __str__(self) -> str:
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        return f"A circle has {self.get_number_of_sides()} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}"
#reference: pycharm itself helped alot with autofill recommendations for the lines of code, adjusted the calculations to follow your instructions instead of pycharms recommended calculations

if __name__ == '__main__':
    rectangle = Rectangle(4, 4.1, 2.3)
    print(rectangle)  # 4 sides, area=9.43, perimeter=12.8

    circle = Circle(1, 3.5)
    print(circle)  # 1 side, area=38.48, perimeter=21.99

    print()

    shapes = [
        Circle(1, 3.2),  # 1 side, area=32.17, perimeter=20.11
        Rectangle(4, 2, 2.6),  # 4 sides, area=5.20, perimeter=9.20
        Circle(1, 8.3),  # 1 side, area=216.42, perimeter=52.15
    ]

    for shape in shapes:
        print(shape)
    print()

    rectangle2 = Rectangle(4, 1, 1)
    rectangle2.set_length(2)
    rectangle2.set_width(4)
    print(rectangle2)  # 4 sides, area=8, perimeter=12
    print(rectangle2.get_length())  # 2
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # 1 side, area=12.57, perimeter=12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2)) # False
    print(circle2 == Circle(1, 2))  # True
