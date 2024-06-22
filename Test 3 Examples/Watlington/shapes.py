class Shape:
    def __init__(self, numer_of_sides):
        self.number_of_sides = numer_of_sides
        #I don't think I'm supposed to take an input here, but I can't tell in the if=main program where the sides are set

    #I'm also not sure if this is what the question is asking but below is my calculate area method
    def calculate_area(self, number_of_sides):
        return self.number_of_sides * number_of_sides
        pass

    def calculate_perimeter(self, number_of_sides):
        # I want the length of each side to be added to the last side input to calculate the perimeter
        for i in len(number_of_sides):
            i += number_of_sides[i]
            return self.number_of_sides
        pass
    def get_num_sides(self):
        return self.number_of_sides

class Rectangle(Shape):
    def __init__(self,number_of_sides, height=1, width=1):
        super().__init__(number_of_sides)
        #Using the super() function to get number of sides from parent class
        self.height = height
        self.width = width

    def calculate_area_rec(self, height, width):
        return self.height * self.width

    def calculate_perimeter_rec(self):
        return 2 * (self.height + self.width)

    def get_width(self, width):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_height(self, height):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def __eq__(self, height, width):
        if self.height == self.new_height and self.width == self.new_width:
            return true
    #I'm not sure about the str method, this is my best guess
    def __str__(self, number_of_sides, calculate_area, calculate_perimeter):
        super().__str__(number_of_sides, calcualte_area, calculate_perimeter)
        return f"A rectangle has {self.number_of_sides} | Area = {self.calculate_area()} | Perimeter = {self.calculate_perimeter()}"


class Circle(Shape):
    def __init__(self, radius, number_of_sides):
        super().__init__(number_of_sides)
        self.radius = radius

    def calculate_area_circ(self, radius):
        return math.pi * self.radius ** 2
    #i hope math.pi is right

    def calculate_perimeter_circ(self, radius):
        return 2 * math.pi * self.radius

    def get_radius_circ(self, radius):
        return self.radius

    def set_radius_circ(self, new_radius):
        self.radius = new_radius

    def __str__(self):
        return f"A circle has {self.number_of_sides} | Area = {self.calculate_area_circ()} | Perimeter = {self.calculate_perimeter_circ()}"


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
