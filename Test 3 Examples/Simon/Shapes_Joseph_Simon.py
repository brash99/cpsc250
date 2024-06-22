import math

class Shape:
    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass  # To be overridden in derived classes

    def calculate_perimeter(self):
        pass  # To be overridden in derived classes

    def set_number_of_sides(self, sides):
        self.__number_of_sides = sides

    def get_number_of_sides(self):
        return self.__number_of_sides

class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        super().__init__(number_of_sides)
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.__width == other.get_width() and self.__height == other.get_height()

    def __str__(self):
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"

class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def __eq__(self, other):
        return isinstance(other, Circle) and self.__radius == other.get_radius()

    def __str__(self):
        return f"A circle has {self.get_number_of_sides()} side | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"

if __name__ == '__main__':
    rectangle = Rectangle(4, 4.1, 2.3)
    print(rectangle)  # Output: A rectangle has 4 sides | Area = 9.43 | Perimeter = 12.80

    circle = Circle(1, 3.5)
    print(circle)  # Output: A circle has 1 side | Area = 38.48 | Perimeter = 21.99

    print()

    shapes = [
        Circle(1, 3.2),     # A circle has 1 side | Area = 32.17 | Perimeter = 20.11
        Rectangle(4, 2, 2.6), # A rectangle has 4 sides | Area = 5.20 | Perimeter = 9.20
        Circle(1, 8.3)      # A circle has 1 side | Area = 216.42 | Perimeter = 52.15
    ]

    for shape in shapes:
        print(shape)
    print()

    rectangle2 = Rectangle(4, 1, 1)
    rectangle2.set_width(4)
    rectangle2.set_height(2)
    print(rectangle2)  # Output: A rectangle has 4 sides | Area = 8.00 | Perimeter = 12.00
    print(rectangle2.get_width())  # Output: 4
    print(rectangle2.get_height())  # Output: 2

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # Output: A circle has 1 side | Area = 12.57 | Perimeter = 12.57
    print(circle2.get_radius())  # Output: 2

    print()

    print(rectangle2 == Rectangle(4, 4, 2))  # Output: False
    print(circle2 == Circle(1, 2))  # Output: True
