class Vehicle:
    def __init__(self, brand="Vehicle", model="Generic"):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


# TODO: complete the Car, Plane, and Boat classes
class Car:
    def __init__(self, brand="Chevrolet", model="Sedan"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print(f"Drive!")

class Plane:
    def __init__(self, brand="Lindbergh", model="Spirit of St. Louis"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print(f"Fly!")


class Boat:
    def __init__(self, brand="Titanic", model="Unsinkable"):
        Vehicle.__init__(self, brand, model)

    def move(self):
        print(f"Sail!")


if __name__ == '__main__':

    user_string = input()
    types = ["car", "plane", "boat"]

    while user_string != "-1":
        tokens = user_string.split()
        vehicle_type = tokens[0]

        if len(tokens) == 3:
            brand = tokens[1]
            model = tokens[2]
            if vehicle_type in types:
                if vehicle_type == "car":
                    vehicle = Car(brand, model)
                elif vehicle_type == "plane":
                    vehicle = Plane(brand, model)
                elif vehicle_type == "boat":
                    vehicle = Boat(brand, model)
                print(f"{vehicle.brand}")
                print(f"{vehicle.model}")
                vehicle.move()
            else:
                print("Unknown vehicle type!!")

        elif len(tokens) == 2:
            brand = tokens[1]
            if vehicle_type in types:
                if vehicle_type == "car":
                    vehicle = Car(brand)
                elif vehicle_type == "plane":
                    vehicle = Plane(brand)
                elif vehicle_type == "boat":
                    vehicle = Boat(brand)
                print(f"{vehicle.brand}")
                print(f"{vehicle.model}")
                vehicle.move()
            else:
                print("Unknown vehicle type!!")
        else:
            if vehicle_type in types:
                if vehicle_type == "car":
                    vehicle = Car()
                elif vehicle_type == "plane":
                    vehicle = Plane()
                elif vehicle_type == "boat":
                    vehicle = Boat()
                print(f"{vehicle.brand}")
                print(f"{vehicle.model}")
                vehicle.move()
            else:
                print("Unknown vehicle type!!")

        user_string = input()

    print('Done!')