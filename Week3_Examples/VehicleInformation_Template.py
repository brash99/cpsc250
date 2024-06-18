class Vehicle:
    def __init__(self, brand="Vehicle", model="Generic"):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


# TODO: complete the Car, Plane, and Boat classes
class Car(Vehicle):

    def __init__(self, brand="Chevrolet", model="Sedan"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print("Drive!")

class Plane(Vehicle):

    def __init__(self, brand="Lindbergh", model="Spirit of St. Louis"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print("Fly!")


class Boat(Vehicle):

    def __init__(self, brand="Titanic", model="Unsinkable"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print("Sail!")



if __name__ == '__main__':
# TODO:  write main program

    user_string = input()

    while user_string != '-1':

        line_elements = user_string.split()
        vehicle_type = line_elements[0]

        if vehicle_type == 'car':
            if len(line_elements) == 3:
                my_car = Car(line_elements[1], line_elements[2])
            elif len(line_elements) == 2:
                my_car = Car(line_elements[1])
            else:
                my_car = Car()

            print(f'{my_car.brand}')
            print(f'{my_car.model}')
            my_car.move()

        elif vehicle_type == 'plane':
            if len(line_elements) == 3:
                my_plane = Plane(line_elements[1], line_elements[2])
            elif len(line_elements) == 2:
                my_plane = Plane(line_elements[1])
            else:
                my_plane = Plane()

            print(f'{my_plane.brand}')
            print(f'{my_plane.model}')
            my_plane.move()

        elif vehicle_type == 'boat':
            if len(line_elements) == 3:
                my_boat = Boat(line_elements[1], line_elements[2])
            elif len(line_elements) == 2:
                my_boat = Boat(line_elements[1])
            else:
                my_boat = Boat()

            print(f'{my_boat.brand}')
            print(f'{my_boat.model}')
            my_boat.move()

        else:
            print("Unknown Vehicle Type!!")

        user_string = input()

    # Do more stuff ... ha! I am done!
    print("Done!")