class Circle:
    def __init__(self, radius=0.0):
        self.radius = radius

    def compute_area(self):
        return 3.14159265*self.radius**2

    def compute_circumference(self):
        return 2.0*3.14159265*self.radius
