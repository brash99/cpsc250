def change_value(x):
    x = x + 1

class Circle:
    def __init__(self,radius):
        self.radius = radius

def append_item(mylist = []) :
    mylist.append(1)
    return mylist


class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    y = 10
    change_value(y)
    print(y)  # Expected Output: 11

    print(append_item())  # Expected Output: [1]
    print(append_item())  # Expected Output: [1, 1]

    c = Circle(5)
    print(c.radius)  # Expected Output: 5
    c.radius = 10
    print(c.radius)  # Expected Output: 10

    buddy = Dog("Buddy")
    print(buddy.__str__)

