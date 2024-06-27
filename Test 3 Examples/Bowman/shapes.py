import math

# Step 1: Make the base class Shape
class Shape:
    def __init__(self, number_of_sides):
        # init the Shape class with a number_of_sides
        self.__number_of_sides = number_of_sides

    def calculate_area(self):
        # this will be used for other derived classes below
        pass

    def calculate_perimeter(self):
        # this will be used for other derived classes below
        pass

    def set_number_of_sides(self, number_of_sides):
        # Setter for the number_of_sides
        self.__number_of_sides = number_of_sides

    def get_number_of_sides(self):
        # Getter for the number_of_sides
        return self.__number_of_sides

# Step 2: Make a derived class Rectangle
class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        # init the Rectangle class by inheriting from the Shape class
        super().__init__(number_of_sides)
        self.__width = width
        self.__height = height

    def calculate_area(self):
        # formula for the area of the rectangle
        return self.__width * self.__height

    def calculate_perimeter(self):
        # formula for the perimeter of the rectangle
        return 2 * (self.__width + self.__height)

    def set_width(self, width):
        # Setter for the width
        self.__width = width

    def get_width(self):
        # Getter for the width
        return self.__width

    def set_height(self, height):
        # Setter for the height
        self.__height = height

    def get_height(self):
        # Getter for the height
        return self.__height

# wanted to make a note that I used chat gpt/copilit to help me write the eq and the str functions because I was having a really dificuilt time understanding
# after learning more about it, I feel confident in the code and what it is doing
    def __eq__(self, other):
        # this function allows me to check the equality of two triangles using width and height
        return self.__width == other.get_width() and self.__height == other.get_height()

    def __str__(self):
        # this will return a string with rectangle info
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"

# Step 3: Make a derived class Circle
class Circle(Shape):
    def __init__(self, number_of_sides, radius):
        # init the Circle class, inheriting from Shape
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self):
        # formula for the area of the circle
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        # formula for the perimeter of the circle
        return 2 * math.pi * self.__radius

    def set_radius(self, radius):
        # Setter for the radius
        self.__radius = radius

    def get_radius(self):
        # Getter for the radius
        return self.__radius
# used the info I learned in the rectangle class to help me with the last two functions
    def __eq__(self, other):
        # this function allows me to check the equality of two circles using their radius
        return self.__radius == other.get_radius()

    def __str__(self):
        # this will return a string with circle info
        return f"A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f} | Perimeter = {self.calculate_perimeter():.2f}"

# Main program to test the classes
# this is from the directions document
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

    print(rectangle2 == Rectangle(4, 4, 2))  # False
    print(circle2 == Circle(1, 2))  # True
