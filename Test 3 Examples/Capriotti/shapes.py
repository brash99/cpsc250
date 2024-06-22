# import math in order to use math.pi
import math

# Step 1: Create base class Shape
# with constructor with a single argument (number of sides)
class Shape:
    # Constructor takes a single argument (number of sides)
    def __init__(self, number_of_sides):
        # class Shape has one private instance variable of type integer named number_of_sides
        # defined in constructor body
        self.__number_of_sides = int(number_of_sides)

    # calculate_area takes no arguments, just passes
    def calculate_area(self):
        pass

    # calculate_perimeter also takes no arguments, just passes
    def calculate_perimeter(self):
        pass

    # Setter method takes one argument (the number of sides) and returns nothing
    def set_number_of_sides(self, number_of_sides):
        self.__number_of_sides = int(number_of_sides)

    # Getter method takes no arguments and returns the number of sides
    def get_number_of_sides(self):
        return self.__number_of_sides


# Step 2: Create a derived class (of the base Shape class) called Rectangle
class Rectangle(Shape):
    # Constructor takes three arguments: number_of_sides, width, and height
    def __init__(self, number_of_sides, width, height):
        # Fulfill the constructor requirement of the parent class
        super().__init__(number_of_sides)
        # Define the width instance variable (private, float) in the constructor body
        self.__width = float(width)
        # Define the height instance variable (private, float) in the constructor body
        self.__height = float(height)

    # Implement the calculate_area method as area of rectangle = width * height
    def calculate_area(self):
        return self.__width * self.__height

    # Implement the calculate_perimeter method as perimeter of rectangle = 2(width) + 2(height)
    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    # Setter method for rectangle width takes one argument (width) and returns nothing
    def set_width(self, width):
        self.__width = float(width)

    # Getter method for rectangle width takes no arguments and returns the width
    def get_width(self):
        return self.__width

    # Setter method for rectangle height takes one argument (height) and returns nothing
    def set_height(self, height):
        self.__height = float(height)

    # Getter method for rectangle height takes no arguments and returns the height
    def get_height(self):
        return self.__height

    # A rectangle is equal to another rectangle if (and only if) BOTH the heights
    # and widths are equal to one another
    # __eq__ method overrides == operator
    # I asked ChatGPT "What is wrong with this program?"
    # I had forgotten that you need to use getter methods to access private variables
    def __eq__(self, other):
        if self.get_height() == other.get_height() and self.get_width() == other.get_width():
            return True
        else:
            return False

    # Returns "A rectangle has x sides | Area = x | Perimeter = x"
    # __str__ method overrides print() function
    def __str__(self):
        return (f"A rectangle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f}"
                f" | Perimeter = {self.calculate_perimeter():.2f}")

# Step 3. Create a class named Circle that is a child of Shape
class Circle(Shape):
    # Create a constructor that takes two arguments: number_of_sides and radius
    def __init__(self, number_of_sides, radius):
        # Fulfill the constructor requirement of the parent class.
        super().__init__(number_of_sides)
        # Define the radius instance variable (private, float) in the constructor body.
        self.__radius = float(radius)

    # Setter method for circle radius takes one argument (radius) and returns nothing
    def set_radius(self, radius):
        self.__radius = float(radius)

    # Getter method for circle radius takes no arguments and returns the radius
    def get_radius(self):
        return self.__radius

    # Implement the calculate_area method as area of a circle = PI * radius^2
    def calculate_area(self):
        return math.pi * self.__radius ** 2

    # Implement the calculate_perimeter method as perimeter (aka circumference)
    # of a circle = 2 * PI * radius
    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    # A circle is equal to another circle if (and only if)
    # the radii are equal to one another
    # __eq__ method overrides == operator
    # I asked ChatGPT "What is wrong with this program?"
    # I had forgotten that you need to use getter methods to access private variables
    def __eq__(self, other):
        if self.get_radius() == other.get_radius():
            return True
        else:
            return False

    def __str__(self):
        return (f"A circle has {self.get_number_of_sides()} sides | Area = {self.calculate_area():.2f}"
                f" | Perimeter = {self.calculate_perimeter():.2f}")

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
