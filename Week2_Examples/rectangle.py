class Rectangle:

    def __init__(self, height=1, width=1):
        self.height = height
        self.width = width

    def _get_area(self):
        return self.height*self.width

    def resize(self, new_height):
        area = self._get_area()
        self.height = new_height
        self.width = area/self.height

    def print_rectangle(self):
        print(f"Height: {self.height:.1f} Width: {self.width:.1f}     Area: {self._get_area():.1f}")


if __name__ == "__main__":

    rectangle = Rectangle(10, 5)
    rectangle.print_rectangle()

    rectangle.resize(2)
    rectangle.print_rectangle()
