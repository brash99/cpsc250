import math
class Shape:

    def __init__(self, sides):
        self.number_of_sides = sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, sides):
        self.number_of_sides = sides

    def get_number_of_sides(self):
        return self.number_of_sides


class Rectangle(Shape):

    def __init__(self, sides, width, length):
        super().__init__(sides)
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def __eq__(self, other):
        return self.length==other.length and self.width==other.width

    def __str__(self):
        return f'A rectangle has {self.number_of_sides} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}'

class Circle(Shape):

    def __init__(self, sides, radius):
        super().__init__(sides)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __eq__(self, other):
        return self.radius==other.radius

    def __str__(self):
        return f'A circle has {self.number_of_sides} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}'

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
    rectangle2.set_height(2)
    rectangle2.set_width(4)
    print(rectangle2)  # 4 sides, area=8, perimeter=12
    print(rectangle2.get_height())  # 2
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # 1 side, area=12.57, perimeter=12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2)) # False
    print(circle2 == Circle(1, 2))  # True
