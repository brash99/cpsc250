import math


# Step 1: Create a base class called Shape
class Shape:
    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def get_number_of_sides(self):
        return self.__number_of_sides


# Step 2: Create a derived class called Rectangle
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
        if isinstance(other, Rectangle):
            return self.__width == other.__width and self.__height == other.__height
        return False

    def __str__(self):
        return (f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | "
                f"Perimeter = {self.calculate_perimeter():.2f}")


# Step 3: Create a class named Circle that is a child of Shape
class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        return False

    def __str__(self):
        return (f"A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | "
                f"Perimeter = {self.calculate_perimeter():.2f}")


# I used the code you provided here
if __name__ == "__main__":
    rectangle = Rectangle(4, 4.1, 2.3)
    print(rectangle)  # 4 sides, area=9.43, perimeter=12.80

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
    print(rectangle2)  # 4 sides, area=8.00, perimeter=12.00
    print(rectangle2.get_height())  # 2
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # 1 side, area=12.57, perimeter=12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2))  # False
    print(circle2 == Circle(1, 2))  # True
