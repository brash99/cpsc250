# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        print(F'   Vehicle Make: {self.vehicle_make}')
        print(F'   Value: {self.vehicle_value}')

#super.init____(
class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.vehicle_model = car_model
        self.vehicle_year = car_year

    def display_info(self):
        print(F'   Description: {self.vehicle_year} {self.vehicle_make} {self.vehicle_model}')
        print(F'   Value: {self.vehicle_value}')


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.vehicle_model = truck_model
        self.vehicle_year = truck_year
        self.is_allwd = is_allwd

    def display_info(self):
        print(f'   Description: {self.vehicle_year} {self.vehicle_make} {self.vehicle_model}')
        print(f'   Value: {self.vehicle_value}')
        print(f'   All Wheel Drive: {self.is_allwd}')

    
# TODO:  Define the display_list() function
def print_list(collection):
    for i in range(len(collection)):
        print(f'Vehicle {i + 1} Information:')
        collection[i].display_info()
        print()


if __name__ == "__main__":

    # TODO: Declare a list called my_collection
    my_collection = []
    user_string = input()
    
    while user_string != 'done':
        tokens = user_string.split()
        vehicle_type = tokens[0]
        vehicle_make = tokens[1]
        vehicle_value = tokens[2]

        if vehicle_type == 'vehicle':
            my_vehicle = Vehicle(vehicle_make,vehicle_value)
            my_collection.append(my_vehicle)
        elif vehicle_type == 'car':
            vehicle_model = tokens[3]
            vehicle_year = tokens[4]
            my_car = Car(vehicle_make, vehicle_value, vehicle_model, vehicle_year)
            my_collection.append(my_car)

        elif vehicle_type == 'truck':
            vehicle_model = tokens[3]
            vehicle_year = tokens[4]
            is_allwd = tokens[5]
            my_truck = Truck(vehicle_make, vehicle_value, vehicle_model, vehicle_year, is_allwd)
            my_collection.append(my_truck)
        else:
            print("Invalid")





        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        user_string = input()

    # TODO: Call the display_list() function
    print_list(my_collection)

# it doesn't run BUT i did not have to use chatgpt