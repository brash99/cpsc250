# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        pass

    def display_info(self):
        pass


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        pass

    def display_info(self):
        pass


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        pass

    def display_info(self):
        pass
    
    
# TODO:  Define the display_list() function

if __name__ == "__main__":

    # TODO: Declare a list called my_collection

    user_string = input()
    
    while user_string != 'done':
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        user_string = input()

    # TODO: Call the display_list() function
