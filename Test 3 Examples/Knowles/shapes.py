import math   #have to let the program know that I am going to use functions of math
class Shape:
    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def calculate_area(self): #passing the next two functions to be called back into the code later on
        pass

    def calculate_perimeter(self):
        pass

    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = number_of_sides  #sets the number of sides

    def get_number_of_sides(self):
        return self.__number_of_sides  #returns the number of sides

class Rectangle(Shape):
    def __init__(self, number_of_sides, width, height):
        super().__init__(number_of_sides) #calls back the number of sides from earlier so that number of sides for all subsequent terms won't have to be rewritten for specificity
        self.__width = width
        self.__height = height

    def calculate_area(self): #this is the area of the rectangle
        return self.__width * self.__height

    def calculate_perimeter(self): #this is the perimeter fo the rectangle
        return 2 * (self.__width + self.__height)

    def set_width(self, width): #calculates the width of the rectangle
        self.__width = width

    def get_width(self):  #returns the width
        return self.__width

    def set_height(self, height): #setter function
        self.__height = height

    def get_height(self):  #getter function
        return self.__height

    def __eq__(self, other):  #checks to see if the width and the height are equal
        if isinstance(other, Rectangle): #used openAI assistance with this line - used for type checking. Was unsure of how to check for equality
            return self.__width == other.__width and self.__height == other.__height
        return False

    def __str__(self):  #returns the formatted string with sides, area, and perimeter
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        return f"A rectangle has {self.get_number_of_sides()} sides | Area = {area} | Perimeter = {perimeter}"

class Circle(Shape): #for the circle, followed the same sort of 'formula' that was used for rectangle.
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.__radius = radius

    def calculate_area(self): #gets area
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self): #gets perimeter
        return 2 * math.pi * self.__radius

    def set_radius(self, radius): #setter function
        self.__radius = radius

    def get_radius(self):  #getter function
        return self.__radius

    def __eq__(self, other): #checks for equality based on the radii
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        return False

    def __str__(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        return f"A circle has {self.get_number_of_sides()} sides | Area = {area} | Perimeter = {perimeter}"

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

