# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make
        self.value = vehicle_value

    def display_info(self):
        print('Vehicle Information:')
        print('   Vehicle Make:', self.make)
        print('    Value:', self.value)


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_model, car_year)
        self.description = (f'{car_year} {car_make} {car_model}')
        self.model = car_model
        self.year = car_year


    def display_info(self):
        print('Vehicle Information:')
        print('   Description:', self.description)
        print('   Value:', self.value)


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.model = truck_model
        self.year = truck_year
        self.is_allwd = is_allwd
        self.description = (f'{truck_year} {truck_make} {truck_model}')

    def display_info(self):
        print('Vehicle Information:')
        print('   Description:', self.description)
        print('   Value:', self.value)
        print('   All Wheel Drive:', self.is_allwd)
    
    
# TODO:  Define the display_list() function

if __name__ == "__main__":
    my_collection = []

    # TODO: Declare a list called my_collection

    user_string = input()
    
    while user_string != 'done':
        parts = user_string.split()
        vehicle_type = parts[0]


        if vehicle_type == 'vehicle':
            make, value = parts[1], int(parts[2])
            my_collection.append(Vehicle(make, value))
        elif vehicle_type == 'car':
            make, value, model, year = parts[1], int(parts[2]), parts[3], int(parts[4])
            my_collection.append(Car(make, value, model, year))
        elif vehicle_type == 'truck':
            make, value, model, is_allwd, = parts[1], int(parts[2]), parts[3], int(parts[4]), parts[5].lower() == 'true'
            my_collection.append(Truck(make, value, model, year, is_allwd))
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        user_string = input()

    # TODO: Call the display_list() function
display_list(my_collection)