import math
# if you are going to use math.pi, you need to import math

class Shape:
    def __init__(self, numer_of_sides):
        self.number_of_sides = numer_of_sides
        #I don't think I'm supposed to take an input here, but I can't tell in the if=main program where the sides are set

    #I'm also not sure if this is what the question is asking but below is my calculate area method
    #original: def calculate_area(self, number_of_sides):
    def calculate_area(self):

    # These methods in the parent class are just passed
    
    #    return self.number_of_sides * number_of_sides
        pass

    #original: def calculate_perimeter(self, number_of_sides):
    def calculate_perimeter(self):
    # These methods in the parent class are just passed

    #    # I want the length of each side to be added to the last side input to calculate the perimeter
    #    for i in len(number_of_sides):
    #        i += number_of_sides[i]
    #        return self.number_of_sides
        pass
    
    #original: def get_num_sides(self):
    def get_number_of_sides(self):
        return self.number_of_sides
    
    # One also needs a setter method!
    def set_number_of_sides(self, sides):
        self.number_of_sides = sides

class Rectangle(Shape):
    #original: def __init__(self,number_of_sides, height=1, width=1):
    def __init__(self,number_of_sides, width, height):
        super().__init__(number_of_sides)
        #Using the super() function to get number of sides from parent class
        self.height = height
        self.width = width

    #original: def calculate_area_rec(self, height, width):
    def calculate_area(self):
        return self.height * self.width

    #original: def calculate_perimeter_rec(self):
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    #original: def get_width(self, width):
    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    #original: def get_height(self, height):
    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    #original: def __eq__(self, height, width):
    def __eq__(self, other):
        if self.height == other.height and self.width == other.width:
            return True
        # you also need to return something if the condition is not met
        else:
            return False

    #I'm not sure about the str method, this is my best guess
    #original: def __str__(self, number_of_sides, calcualte_area, calculate_perimeter):
    def __str__(self):
        # The following line is not what the question is asking for
        #super().__str__(number_of_sides, calcualte_area, calculate_perimeter)
        #original: return f"A rectangle has {self.number_of_sides} | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"
        return f"A rectangle has {self.number_of_sides} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"


class Circle(Shape):
    #original: def __init__(self, radius, number_of_sides):
    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides)
        self.radius = radius

    #original: def calculate_area_circ(self, radius):
    def calculate_area(self):
        return math.pi * self.radius ** 2
    #i hope math.pi is right

    #original: def calculate_perimeter_circ(self, radius):
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    #original: def get_radius_circ(self, radius):
    def get_radius(self):
        return self.radius

    #original: def set_radius_circ(self, new_radius):
    def set_radius(self, new_radius):
        self.radius = new_radius

    def __str__(self):
        #original: return f"A circle has {self.number_of_sides} | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"
        return f"A circle has {self.number_of_sides} sides | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"

    # You also need to implement the __eq__ method for the Circle class
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

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
