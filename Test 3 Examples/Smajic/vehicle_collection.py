# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        print(f" Vehicle Make: {self.vehicle_make}")
        print(f" Value: {self.vehicle_value}")



class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.car_model = car_model
        self.car_year = car_year

    def display_info(self):
        print(f" Description: {self.car_year} {self.vehicle_make} {self.car_model}")
        print(f" Value: {self.vehicle_value}")


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd #all wheel drive

    def display_info(self):
        print(f" Description: {self.truck_year} {self.vehicle_make} {self.truck_model}")
        print(f" Value: {self.vehicle_value}")
        print(f" All Wheel Drive: {self.is_allwd}")

# TODO:  Define the display_list() function
def display_list(my_collection):
    for i, vehicle in enumerate(my_collection, 1):
        print(f"Vehicle {i} Information:")
        vehicle.display_info()
#pycharm helped with code recommendations, not sure if that counts as a reference
if __name__ == "__main__":
    my_collection = []
    while True: #not sure if I supposed to the modify the given code
        user_input = input().strip() #reference copilot used to help with formatting the first part of code
        if user_input == "done":
            break
        type = user_input.split() #split the user variable
        if type[0] == "vehicle": #object type
            my_collection.append(Vehicle(type[1], int(type[2]))) #append to add to list
        elif type[0] == "car":
            my_collection.append(Car(type[1], int(type[2]), type[3], int(type[4])))
        elif type[0] == "truck":
            my_collection.append(Truck(type[1], int(type[2]), type[3], int(type[4]), type[5] == "true"))

    display_list(my_collection)
        # TODO: Check if input is a vehicle, car, or truck
        #Split the user_string input into variables
        #Store as an object of the appropriate type
        #Add to the list my_collection

    # TODO: Call the display_list() function
