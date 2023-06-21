import math


class Circle:
    def __init__(self, radius=0.0):
        self.radius = radius

    def compute_area(self):
        return math.pi*self.radius**2

    def compute_circumference(self):
        return 2.0*math.pi*self.radius
