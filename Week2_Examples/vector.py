import math


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def _magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def __str__(self):
        print(f'({self.x}, {self.y}, {self.z})')

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __eq__(self, value):
        # print(self._magnitude(),value)
        return self._magnitude() == value


if __name__ == "__main__":

    a = Vector(1.0, 2.0, -1.0)
    b = Vector(-4.0, 3.0, -0.0)

    c = a*b

    if ((c == 0) and (a == 5)) or (b == 5):
        print('Failure')

    print(c)
