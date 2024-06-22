import math
#I imported math so I could use math.pi
class Shape:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
    def setter_number_of_sides(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def getter_number_of_sides(self):
        return self.number_of_sides


class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        super().__init__(number_of_sides)
        self.number_of_sides = number_of_sides
        self.width = width
        self.height = height
    def calc_area(self):
        area = self.width * self.height
        return area

    def calc_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def __eq__(self, another):
        return self.width == another.width and self.height == another.height

    def __str__(self):
        return f"A rectangle has {self.getter_number_of_sides()} sides | Area = {self.calc_area():.2f} | Perimeter = {self.calc_perimeter():.2f}"




class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.radius = radius

    def calc_area(self):
        circle_area = math.pi * self.radius ** 2
        return circle_area

    def calc_perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter
    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __eq__(self, another):
        return self.radius == another.radius
    def __str__(self):
        return f"A circle has {self.getter_number_of_sides()} side | Area = {self.calc_area():.2f} | Perimeter = {self.calc_perimeter():.2f}"



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
