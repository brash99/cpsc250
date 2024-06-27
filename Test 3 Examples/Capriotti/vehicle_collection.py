# Base class Vehicle is initiated with variables vehicle_make (default is empty string)
# and vehicle_value (default is 0).
# Function display_info prints vehicle make and value.
class Vehicle:
    def __init__(self, vehicle_make='', vehicle_value=0):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

# Print vehicle make, then value (each line indented)
    def display_info(self):
        print(f'   Vehicle Make: {self.vehicle_make}')
        print(f'   Value: {self.vehicle_value}')

# class Car is derived from class Vehicle. It is initiated with variables car_make,
# car_value, car_model, and car_year. Defaults are either 0 or an empty string.
class Car(Vehicle):
    def __init__(self, car_make='', car_value=0, car_model='', car_year=0):
        super().__init__(car_make, car_value)
        self.car_make = car_make
        self.car_value = car_value
        self.car_model = car_model
        self.car_year = car_year

    # Print car year, make, and model, then value (each line indented)
    def display_info(self):
        print(f'   Description: {self.car_year} {self.car_make} {self.car_model}')
        print(f'   Value: {self.car_value}')

# class Truck is derived from class Car. It is initiated with variables truck_make,
# truck_value, truck_model, truck_year and is_allwd. Defaults are either 0 or an empty string.
# I thought about instantiating is_allwd as a boolean variable, but I wanted to be able to
# set 'Unknown' as the default.
class Truck(Car):
    def __init__(self, truck_make='', truck_value=0, truck_model='', truck_year=0, is_allwd=''):
        super().__init__(truck_make, truck_value, truck_model, truck_year)
        self.truck_make = truck_make
        self.truck_value = truck_value
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

    # Print truck year, make, and model, then value, then if the truck has
    # all wheel drive or not (each line indented)
    def display_info(self):
        super().display_info()
        print(f'   All Wheel Drive: {self.is_allwd}')


# This function is copied from PlantInformation_Functions.py
# For each item in a list, it prints the item's index # (plus 1)
# Then calls that item's class-specific display_info() function
# Then outputs a newline for readability
def display_list(lst):
    for i in range(len(lst)):
        num = i + 1
        print(f'Vehicle {num} Information:')
        lst[i].display_info()
        print()

if __name__ == "__main__":

    # Declare a list called my_collection
    my_collection = []

    # Get the first vehicle's information
    user_string = input("Enter vehicle type (vehicle, car, or truck), make, and value, separated by spaces.\n"
                        "If the vehicle is a car or truck, also enter model and year, also separated by spaces.\n"
                        "If the vehicle is a truck, also enter 'true' if the truck has all wheel drive and 'false' if it does not.\n"
                        "Enter all of a single vehicle's information on one line, then press enter.\n").strip()

    while user_string != 'done':
        # Split the user_string input into variables
        user_tokens = user_string.split()
        # The first token should be the type of vehicle (vehicle, car, or truck)
        # This line of code is copied from PlantFlower.py
        vehicle_type = user_tokens[0]
        # The second token should be the make of the vehicle.
        if len(user_tokens) > 1:
            vehicle_make = user_tokens[1]
        # If there is no second token, vehicle_make is set to 'Unknown' to avoid an error
        # when instantiating a Vehicle object.
        else:
            vehicle_make = 'Unknown'
        # The third token should be the value of the vehicle.
        if len(user_tokens) > 2:
            vehicle_value = user_tokens[2]
        # If there is no third token, vehicle_value is set to 0 to avoid an error
        # when instantiating a Vehicle object.
        else:
            vehicle_value = 0
        # Check if input is a vehicle, car, or truck
        # Store as an object of the appropriate type
        # Add to the list my_collection
        # Check if input is a vehicle
        if vehicle_type == 'vehicle':
            # Store as vehicle object
            my_vehicle = Vehicle(vehicle_make, vehicle_value)
            # Add to the list my_collection
            my_collection.append(my_vehicle)
        # Check if input is a car or truck
        elif vehicle_type == 'car' or vehicle_type == 'truck':
            # The fourth token should be the model of the vehicle.
            if len(user_tokens) > 3:
                vehicle_model = user_tokens[3]
            # If there is no fourth token, vehicle_model is set to 'Unknown' to avoid an error
            # when instantiating a Vehicle object.
            else:
                vehicle_model = 'Unknown'
            #The fifth token should be the vehicle year
            if len(user_tokens) > 4:
                vehicle_year = user_tokens[4]
            # If there is no fifth token, vehicle_year is set to 0 to avoid an error
            # when instantiating a Vehicle object.
            else:
                vehicle_year = 0
            #If the vehicle type is 'car', that should be all of the information.
            if vehicle_type == 'car':
                # Store as car object
                my_car = Car(vehicle_make, vehicle_value, vehicle_model, vehicle_year)
                # Add to the list my_collection
                my_collection.append(my_car)
            #If the vehicle type is 'truck', it also needs to know if the truck has all wheel drive
            if vehicle_type == 'truck':
                #The sixth token should be whether the truck has all wheel drive (true) or not (false)
                if len (user_tokens) > 5:
                    vehicle_isallwd = user_tokens[5]
                # If there is no sixth token, vehicle_isallwd is set to 'Unknown' to avoid an error
                # when instantiating a truck object.
                else:
                    vehicle_isallwd = 'Unknown'
                # Store as truck object
                my_truck = Truck(vehicle_make, vehicle_value, vehicle_model, vehicle_year, vehicle_isallwd)
                # Add to the list my_collection
                my_collection.append(my_truck)

        else:
            print("Invalid vehicle type. Please enter vehicle, car, or truck.")

        # Get the next vehicle's information
        user_string = input("Enter the next vehicle's information, or 'done' to finish.\n").strip()

    display_list(my_collection)
