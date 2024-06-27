import math


# Step 1: Create the base class Shape
# this class does a template for shapes with an attribute for the number of sides
class Shape:
    def __init__(self, number_of_sides: int):
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides: int):
        self.__number_of_sides = number_of_sides

    def get_number_of_sides(self) -> int:
        return self.__number_of_sides


# Step 2: Create the derived class Rectangle
# The Rectangle class which takes from the Shape class, defines a rectangle with width and height attributes
class Rectangle(Shape):
    def __init__(self, number_of_sides: int, width: float, height: float):
        super().__init__(number_of_sides)
        self.__width = width
        self.__height = height

    def calculate_area(self) -> float:
        return self.__width * self.__height

    def calculate_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def set_width(self, width: float):
        self.__width = width

    def get_width(self) -> float:
        return self.__width

    def set_height(self, height: float):
        self.__height = height

    def get_height(self) -> float:
        return self.__height

    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.__width == other.__width and self.__height == other.__height
        return False

# chatgpt helped me with this def below
    def __str__(self) -> str:
        return (f"A rectangle has {self.get_number_of_sides()} sides | "
                f"Area = {self.calculate_area():.2f} | "
                f"Perimeter = {self.calculate_perimeter():.2f}")


# Step 3: Create the derived class Circle
# The Circle class taking from Shape class defines a circle with a radius attribute implements methods to calculate its area and perimeter
class Circle(Shape):
    def __init__(self, number_of_sides: int, radius: float):
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def set_radius(self, radius: float):
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius

    def __eq__(self, other) -> bool:
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        return False
# chatgpt helped me with this def below
    def __str__(self) -> str:
        return (f"A circle has {self.get_number_of_sides()} sides | "
                f"Area = {self.calculate_area():.2f} | "
                f"Perimeter = {self.calculate_perimeter():.2f}")


# Main program to test the classes
if __name__ == '__main__':
    rectangle = Rectangle(4, 4.1, 2.3)
    print(rectangle)  # 4 sides, area=9.43, perimeter=12.8

    circle = Circle(1, 3.5)
    print(circle)  # 1 side, area=38.48, perimeter=21.99

    print()
    shapes = [
        Circle(1, 3.2),
        Rectangle(4, 2, 2.6),
        Circle(1, 8.3),
    ]

    for shape in shapes:
        print(shape)

    print()
    rectangle2 = Rectangle(4, 1, 1)
    rectangle2.set_height(2)
    rectangle2.set_width(4)
    print(rectangle2)
    print(rectangle2.get_height())
    print(rectangle2.get_width())

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)
    print(circle2.get_radius())

    print()
    print(rectangle2 == Rectangle(4, 4, 2))
    print(circle2 == Circle(1, 2))
