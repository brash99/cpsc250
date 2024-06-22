class Shape:
    def __init__(self, number_of_sides): # intialize constructor with number of sides variable
        self.number_of_sides = number_of_sides

    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    # create getter and setter methods
    def set_number_of_sides(self, number_of_sides):
        self.number_of_sides = number_of_sides
    def get_number_of_sides(self):
        return self.number_of_sides
class Rectangle(Shape):
# initialize constuctor with variables of rectangle, I used chat gpt to help me write this
    def __init__(self, number_of_sides, width, height):
        super().__init__(number_of_sides)
        self.width = width
        self.height = height
    # create calculate area method
    def calculate_area(self):
        return self.width * self.height
    # create calculate perimeter method
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


    #create setter and getter methods for width and height
    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def __eq__(self, second_rectangle):
    # __eq__ method, I used chat gpt to help me write this method
        if isinstance(second_rectangle, Rectangle):
            return self.width == second_rectangle.get_width() and self.height == second_rectangle.get_height()
        return False
    def __str__(self):
        #print rectangle info method
        return f'A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}'
import math
class Circle(Shape):
    # initialize the constructor with variables for circle, I used chat gpt to help me write this
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    # getter and setter methods
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    #eq method, I used chat gpt to help me write this method
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_radius() == other.get_radius()
        return False
    #formatted string method
    def __str__(self):
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
