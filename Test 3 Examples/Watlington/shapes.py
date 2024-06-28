
import math

class Shape:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self,sides):
        self.number_of_sides = sides

    def get_number_of_sides(self):
        return self.number_of_sides


#order of height and width incorrect
class Rectangle(Shape):
    def __init__(self,number_of_sides, width, height):
        super().__init__(number_of_sides)
        #Using the super() function to get number of sides from parent class
        self.height = height
        self.width = width

    #use intern parameters and should be calculate_area
    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
    #get functions do not pass in parameters

    def set_width(self, new_width):
        self.width = new_width

    def get_width(self):
        return self.width

    #same thing

    def set_height(self, new_height):
        self.height = new_height

    def get_height(self):
        return self.height


    #do not take parameters
    def __eq__(self, other):
        if self.height == other.height and self.width == other.width:
            return True
        else:
            return False

    #doesn't take parameters
    def __str__(self):
        return f"A rectangle has 4 sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"

class Circle(Shape):

    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __str__(self):
        return f"A circle has {self.number_of_sides} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"


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
    # ^ was originally set_length, I changed it to width so program could run
    rectangle2.set_width(4)
    print(rectangle2)  # 4 sides, area=8, perimeter=12
    print(rectangle2.get_length())  # 2
    # ^ again was using length
    print(rectangle2.get_width())  # 4

    circle2 = Circle(1, 1)
    circle2.set_radius(2)
    print(circle2)  # 1 side, area=12.57, perimeter=12.57
    print(circle2.get_radius())  # 2
    print()

    print(rectangle2 == Rectangle(4, 4, 2)) # False
    print(circle2 == Circle(1, 2))  # True
