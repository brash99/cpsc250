import math


class Shape:
    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides):
        return

    def get_number_of_sides(self):
        return self.__number_of_sides

class Rectangle(Shape):
    def __init__(self, number_of_sides: int, width: float, height: float):
        super().__init__(number_of_sides)
        self.__width = width
        self.__height = height


    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return (2*self.__width) + (2*self.__height)

    def set_width(self, width):
        return

    def set_height(self, height):
        return

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.__width == other.get_width() and self.__height == other.get_height()


    def __str__(self):
        return (f"A rectangle has {self.get_number_of_sides():.2f} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}")



class Circle(Shape):
    def __init__(self, number_of_sides:int , radius:float):
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def set_radius(self, radius):
        return

    def get_radius(self):
        return self.__radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            # print(f'{self.__radius} | {other.get_radius()}') #radii are not the same
            return self.__radius == other.get_radius()


    def __str__(self):
        return (f'A circle has {self.get_number_of_sides():.2f} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f} ')




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
    rectangle2.set_height(2) #changed to set_height instead of set_length
    rectangle2.set_width(4)
    print(rectangle2)  # 4 sides, area=8, perimeter=12
    print(rectangle2.get_height())  # 2 #changed to get_height instead of get_length
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # 1 side, area=12.57, perimeter=12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2)) # False
    print(circle2 == Circle(1, 2))  # True (RADII ARE NOT THE SAME)
