import math

class Circle:

    # When a circle object is created, we have two options:
    # 1. We can create a circle object with a radius value
    # 2. We can create a circle object without a radius value
    # If we create a circle object without a radius value, the default value of the radius is 0.0

    def __init__(self, radius=0.0):
        self.radius = radius

    # Define a method to calculate the area of the circle
    # This function will NOT take any parameters when we
    # call it. It will use the radius value that is stored
    # in the object to calculate the area of the circle
    def compute_area(self):
        return math.pi*self.radius**2

    # Define a method to calculate the circumference of the circle
    # This function will NOT take any parameters when we call it.
    # It will use the radius value that is stored in the object to
    # calculate the circumference of the circle
    def compute_circumference(self):
        return 2.0*math.pi*self.radius

    # Define a method to get the radius of the circle
    # This function will NOT take any parameters when we call it.
    # It will return the radius value that is stored in the object
    def get_radius(self):
        return self.radius

    # Define a method to set the radius of the circle
    # This function will take a single parameter, radius, when we call it.
    # It will set the radius value that is stored in the object to the value
    # that we pass in as a parameter
    def set_radius(self, radius):
        self.radius = radius

    # Define a str method to return a string representation of the object
    # This function MUST NOT take any parameters when we call it.
    # It will return a string that includes the radius value that is stored in the object
    # This function is called when we use the print function to print the object
    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    # Define an eq method to compare two objects
    # This function will take two parameters when we call it:
    # self: The first Circle object
    # other: The second Circle object
    # It will compare the radius value of the two objects
    # It will return True if the radius value of the two objects is the same
    # It will return False if the radius value of the two objects is different
    def __eq__(self, other):
        return self.radius == other.radius
