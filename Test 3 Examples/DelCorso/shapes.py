import math
# I believe I need math for pi

class Shape:
    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
    # these will be given by the actual shapes.

    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = number_of_sides
    # changes number of sides

    def get_number_of_sides(self):
        return self.__number_of_sides
    # a lot of functions for just basic shapes so no need for great detail yet.


class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        super().__init__(number_of_sides)
        self.__width = width
        self.__height = height
        # calls the inside shape class and gets more variables.

    def calculate_area(self):
        return self.__width * self.__height
    # area of a rectangle formula

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)
    # perimeter formula for a retangle

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height
    # both width and height adjusting

    def __eq__(self, other):
        return self.__width == other.get_width() and self.__height == other.get_height()
    # checks to see if both shapes are equal dimensions

    def __str__(self):
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"
    # everything about the rectangle.


class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.__radius = radius
        # like rectangle, super calls inside shape class and gives a variable


    def calculate_area(self):
        return math.pi * self.__radius ** 2
    # math is used to get pi, pi r squared.. pi r squared.. is the area.. inside there.

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius
    # the circumference or perimeter of a circle.

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    # like rectangle gets specific info on variable

    def __eq__(self, other):
        return self.__radius == other.get_radius()
    # checks to see if both shapes are equal dimensions

    def __str__(self):
        return f"A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"
    # returns the info on what the circle is like.


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
