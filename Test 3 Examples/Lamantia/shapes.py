class Shape:
    def __init__(self, number_of_sides):  #Defined number of sides
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass  #No implementation

    def calculate_perimeter(self):
        pass  #No implementation

    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def get_number_of_sides(self):
        return self.__number_of_sides  #Returns number of sides


class Rectangle(Shape):
    def __init__(self, number_of_sides, length, width):  #Defined rectangle shape
        super().__init__(number_of_sides)
        self.__length = length
        self.__width = width

    def calculate_area(self):  #Calculated rectangle area
        return self.__length * self.__width

    def calculate_perimeter(self):  #Calculated rectangle perimeter
        return 2 * (self.__length + self.__width)

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def __eq__(self, other):  #eq method
        return isinstance(other, Rectangle) and self.__length == other.__length and self.__width == other.__width

    def __str__(self):  #str method
        return f'A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}'

import math
class Circle(Shape):
    def __init__(self, number_of_sides, radius):  #Defined circle shape
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2  #Calculated area of circle

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius  #Circumference of circle

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def __eq__(self, other):  #eq method
        return isinstance(other, Circle) and self.__radius == other.__radius

    def __str__(self):  #str method
        return f'A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}'


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
