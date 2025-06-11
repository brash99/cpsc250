#Write a class called Rectangle that has:
#	Two instance variables: width and height
#	A constructor
#	Getters and setters for both variables
#	A method area() that returns the area
#	A __str__() method that returns a string like: "Rectangle(width=3, height=4)"

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self._width + other._width, self._height + other._height)
        return NotImplemented


if __name__ == "__main__":
    rect = Rectangle(3, 4)
    print(rect)  # Expected Output: Rectangle(width=3, height=4)
    print(f"Area: {rect.area()}")  # Expected Output: Area: 12

    rect.set_width(5)
    rect.set_height(6)

    print(rect)  # Expected Output: Rectangle(width=5, height=6)
    print(f"Area: {rect.area()}")  # Expected Output: Area: 30

    rect2 = Rectangle(2, 3)
    rect3 = rect + rect2
    print(rect3)  # Expected Output: Rectangle(width=7, height=9)
