
# TODO:  write the __init__ and display_info functions for the classes
# implementing classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        print(f'Vehicle make: {self.vehicle_make}')
        print(f'Vehicle value: {self.vehicle_value}')

# initialize vehicle make and value
class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.car_model = car_model
        self.car_year = car_year

    def display_info(self):
        print(f'Description: {self.car_year} {self.car_make} {self.car_model}')
        print(f'Value: {self.vehicle_value}')

#
class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd
    def display_info(self):
        print(f'Description: {self.truck_year} {self.truck_make} {self.truck_model}')
        print(f'Value: {self.vehicle_value}')
        print(f'All Wheel Drive: {self.is_allwd}')
    
    
# TODO:  Define the display_list() function
#iterate through collection and calls display info for each
def display_list(collection):
    for index, vehicle in enumerate(collection):
        print(f'Vehicle {index} Information:')
        vehicle.display_info()
        #for separation
        print()

if __name__ == "__main__":

    # TODO: Declare a list called my_collection
    my_collection= []

    user_string = input()
    
    while user_string != 'done':
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        #While loop that keeps going until done, split string to store in parts
        parts = user_string.split()
        #checks length of parts
        if len(parts) == 3:
            type = parts[0]
            make = parts[1]
            model = parts[2]

            if type.lower() == 'vehicle':
                vehicle = Vehicle(type, make, model)
                my_collection.append(vehicle)
            elif type.lower() == 'car':
                car = Vehicle(type, make, model)
                my_collection.append(car)
            elif type.lower() == 'truck':
                truck = Vehicle(type, make, model)
                my_collection.append(truck)


    # TODO: Call the display_list() function
    display_list(my_collection)
