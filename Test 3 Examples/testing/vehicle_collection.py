# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        print(f'   Vehicle Make: {self.vehicle_make}')
        print(f'   Value: {self.vehicle_value}')


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        Vehicle.__init__(self, car_make, car_value)
        self.model = car_model
        self.year = car_year

    def display_info(self):
        print(f'   Description: {self.year} {self.vehicle_make} {self.model}')
        print(f'   Value: {self.vehicle_value}')


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        Vehicle.__init__(self, truck_make, truck_value)
        self.model = truck_model
        self.year = truck_year
        self.is_allwd = is_allwd

    def display_info(self):
        print(f'   Description: {self.year} {self.vehicle_make} {self.model}')
        print(f'   Value: {self.vehicle_value}')
        print(f'   All Wheel Drive: {self.is_allwd}')
    
    
# TODO:  Define the display_list() function

def display_list(collection):
    for i in range(len(collection)):
        print(f'Vehicle {i + 1} Information:')
        collection[i].display_info()
        print()

if __name__ == "__main__":

    # TODO: Declare a list called my_collection

    my_collection = []
    user_string = input()
    
    while user_string != 'done':
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection

        tokens = user_string.split()
        type = tokens[0]
        make = tokens[1]
        value = tokens[2]

        if type == 'vehicle':
            my_vehicle = Vehicle(make, value)
            my_collection.append(my_vehicle)
        elif type == 'car':
            model = tokens[3]
            year = tokens[4]
            my_car = Car(make, value, model, year)
            my_collection.append(my_car)
        elif type == 'truck':
            model = tokens[3]
            year = tokens[4]
            is_4wd = tokens[5]
            my_truck = Truck(make, value, model, year, is_4wd)
            my_collection.append(my_truck)

        user_string = input()

    # TODO: Call the display_list() function
    display_list(my_collection)
