import math
class Shape:
    def __init__(self, number_of_sides):
        self.sides = number_of_sides #initialzie number of sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides):
        self.sides = number_of_sides #initialzie number of sides

    def get_number_of_sides(self):
        return self.sides #initialzie number of sides


class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        self.width = width #initialze width
        self.height = height #initizlize height

    def calculate_area(self):
        return self.width * self.height #returning area

    def calculate_perimeter(self):
        return 2 * (self.width + self.height) #returning perimeter

    def set_width(self, width):
        self.width = width #initialize width

    def get_width(self):
        return self.width #return width

    def set_height(self, height):
        self.height = height #initialize height

    def get_height(self):
        return self.height #return height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __str__(self):
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"


class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        self.radius = radius #initialize radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2) #return area

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius #return perimeter

    def set_radius(self, radius):
        self.radius = radius #initialzie radius

    def get_radius(self):
        return self.radius #return radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f"A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"


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
