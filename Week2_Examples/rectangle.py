class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def _get_area(self):
        return self.length*self.width

    def resize(self, new_length):
        area = self._get_area()
        self.length = new_length
        self.width = area/self.length

    def print_rectangle(self):
        print(f"Length: {self.length:.1f} Width: {self.width:.1f}     Area: {self._get_area():.1f}")


if __name__ == "__main__":

    rectangle = Rectangle(10, 5)
    rectangle.print_rectangle()

    rectangle.resize(2)
    rectangle.print_rectangle()
