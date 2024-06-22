#importing mah function so math.pi will work as pi
import math
class Shape:
    #defining shape attributes
    def __init__(selfself, number_of_sides):
        self.number_of_sides = number_of_sides
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def set_number_of_sides(self, number_of_sides):
        self.number_of_sides = number_of_sides
    def get_number_of_sides(self):
        return self.number_of_sides

class Rectangle(Shape):
    #defining rectangle shape attributes
    def __init__(self, number_of_sides, width, height):
        self.number_of_sides = number_of_sides
        self.width = width
        self.height = height
    #finding area and perimeter
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    #setting the widths and heights as well as returning them
    def set_width(self, width):
        self.width = width
    def get_width(self):
        return self.width
    def set_height(self, height):
        self.height = height
    def get_height(self):
        return self.height
    #comparing two rectangles to see if they are the same
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.width == other.width and self.height == other.height
    #returning rectangles information
    def __str__(self):
        return f'A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}'

class Circle(Shape):
    #defining circle shape attributes
    def __init__(self, number_of_sides, radius):
        self.number_of_sides = number_of_sides
        self.radius = radius
    #finding area and perimeter
    def calculate_area(self):
        return math.pi * self.radius * self.radius
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    #setting the radius as well as returning it
    def set_radius(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    #comparing two circles to see if they are the same
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius
    #returning circles information
    def __str__(self):
        return f'A circle has {self.get_number_of_sides()} side | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}'

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

