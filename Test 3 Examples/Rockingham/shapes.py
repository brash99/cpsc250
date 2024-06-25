import math  # Import Math Module

class Shape:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides  # Init num of sides

    def calculate_area(self):
        pass  # Placeholder

    def calculate_perimeter(self):
        pass    # Placeholder

    def given_num_of_sides(self, num_of_sides):
        self.num_of_sides = num_of_sides  # Set method for num of sides

    def get_num_of_sides(self):
        return self.num_of_sides  # Get method for num of sides

class Rectangle(Shape):
    def __init__(self, num_of_sides, width, length):
        super().__init__(num_of_sides)
        self.__width = width  # Attribute for Width
        self.__length = length  # Attribute for length

    def calculate_area(self):
        return self.__width * self.__length  # Calc Area of Rect

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__length)  # Calc Perim of Rect

    def set_width(self, width):
        self.__width = width  # Set Method

    def get_width(self):
        return self.__width  # Get Method

    def set_length(self, length):
        self.__length = length  # Set Method

    def get_length(self):
        return self.__length  # Get Method

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.__width == other.__width and self.__length == other.__length
        return False

    def __str__(self):
        return f"A rectangle has {self.get_num_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"


class Circle(Shape):
    def __init__(self, num_of_sides, radius):
        super().__init__(num_of_sides)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)  # Calc Area

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius  # Calc Perim

    def set_radius(self, radius):
        self.__radius = radius  # Set Method

    def get_radius(self):
        return self.__radius  # Get Method

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        return False

    def __str__(self):
        return f"A circle has {self.get_num_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"

if __name__ == '__main__':
    rectangle = Rectangle(4, 4.1, 2.3)
    print(rectangle)  # A rectangle has 4 sides | Area = 9.43 | Perimeter = 12.80

    circle = Circle(1, 3.5)
    print(circle)  # A circle has 1 sides | Area = 38.48 | Perimeter = 21.99

    print()

    shapes = [
        Circle(1, 3.2),  # A circle has 1 sides | Area = 32.17 | Perimeter = 20.11
        Rectangle(4, 2, 2.6),  # A rectangle has 4 sides | Area = 5.20 | Perimeter = 9.20
        Circle(1, 8.3),  # A circle has 1 sides | Area = 216.42 | Perimeter = 52.15
    ]

    for shape in shapes:
        print(shape)
    print()

    rectangle2 = Rectangle(4, 1, 1)
    rectangle2.set_length(2)  # Use set_length instead of set_height
    rectangle2.set_width(4)
    print(rectangle2)  # A rectangle has 4 sides | Area = 8.00 | Perimeter = 12.00
    print(rectangle2.get_length())  # 2
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # A circle has 1 sides | Area = 12.57 | Perimeter = 12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2))  # False
    print(circle2 == Circle(1, 2))  # True
