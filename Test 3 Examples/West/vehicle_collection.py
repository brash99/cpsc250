# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        # creating variables for vehicle_make and vehicle_value
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        #Creating formatted return statement for displaying info
        return f"Vehicle Make: {self.vehicle_make}\nValue: {self.vehicle_value}"


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        # directly calling the instructor and assigning variables, i used chat gpt to help me figure out that i can directly call the constructor
        Vehicle.__init__(self, car_make, car_value)
        self.car_model = car_model
        self.car_year = car_year


    def display_info(self):
        # formatted info to display for the car
        return f"Description: {self.car_year} {self.vehicle_make} {self.car_model}\nValue: {self.vehicle_value}"


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        #directly calling the instructor and assigning variables, i used chat gpt to help me figure out that i can directly call the constructor
        Vehicle.__init__(self, truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

    def display_info(self):
        # formattex info to display for trucks
        return f"Description: {self.truck_year} {self.vehicle_make} {self.truck_model}\nValue: {self.vehicle_value}\nAll Wheel Drive: {self.is_allwd}"
    
    
# TODO:  Define the display_list() function
def display_list(collection):
    for i, vehicle in enumerate(collection, start=1): # i used chat gpt to help me get this condensed line of code with the enumerate method
        print(f"Vehicle {i} Information:")
        print(f'{vehicle.display_info()} ') #formatted line to add space
if __name__ == "__main__":

    # TODO: Declare a list called my_collection
    my_collection = []
    user_string = input()
    
    while user_string != 'done':
        parts = user_string.split(' ')
        vehicle_type = parts[0]

        # TODO: Check if input is a vehicle, car, or truck and then assigning corresponding information, i used chat gpt to help me put the indexes together

        if vehicle_type == 'vehicle':
            make = parts[1]
            value = float(parts[2])
            my_collection.append(Vehicle(make, value))
        elif vehicle_type == 'car':
            make = parts[1]
            value = float(parts[2])
            model = parts[3]
            year = int(parts[4])
            my_collection.append(Car(make, value, model, year))
        elif vehicle_type == 'truck':
            make = parts[1]
            value = float(parts[2])
            model = parts[3]
            year = int(parts[4])
            is_allwd = parts[5].lower() == 'true'
            my_collection.append(Truck(make, value, model, year, is_allwd))
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        # get another input
        user_string = input()
        # call display list function with my_collection
    display_list(my_collection)
