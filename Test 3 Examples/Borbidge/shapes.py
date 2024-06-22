import math

class Shape:
    #number_of_sides = int(input()) #old inputs i referenced in email
    
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
     
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    
    def set_number_of_sides(self, number_of_sides):
        self.number_of_sides = number_of_sides
        
    def get_number_of_sides(self):
        return self.number_of_sides

class Rectangle(Shape):
    #width = float(input()) #old inputs referenced in email
    #height = float(input())
    
    def __init__(self, number_of_sides, width, length):
        super().__init__(number_of_sides) #chat gpt for format of super
        self.number_of_sides = number_of_sides
        self.width = width
        self.length = length
        
    def calculate_area(self):
        area = self.width * self.length
        return area
    
    def calculate_perimeter(self):
        perimeter = 2*self.width + 2*self.length
        return perimeter
    
    def set_width(self, width):
        self.width = width
    
    def get_width(self):
        return self.width

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def __eq__(self, other):
        if isinstance(other, Rectangle): #built in ai reminded me how to format the other and Rectangle
            if (self.width == other.width) and (self.length == other.length): #format for this was built in ai
                return True
    def __str__(self):
        area = self.calculate_area() #chat gpt told me to do do this instead of just self.area
        perimeter = self.calculate_perimeter() #chat gpt told me to do do this instead of just self.perimeter
        return f'A rectangle has {self.number_of_sides} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'


class Circle(Shape):
    #radius = float(input()) #old input referenced in email

    def __init__(self, number_of_sides, radius):
        super().__init__(number_of_sides) #chat gpt reminded me of the format for super
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius #chat gpt gave me proper math.pi format
        return perimeter

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __eq__(self, other):
        if isinstance(other, Circle): #chat gpt gave me this line and told me how it works
            if (self.radius == other.radius):
                return True

    def __str__(self):
        area = self.calculate_area() #chat gpt
        perimeter = self.calculate_perimeter() #chat gpt
        return f'A circle has {self.number_of_sides} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'

#i made the floats output with 2 decimal places because it was in the given main statement

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
