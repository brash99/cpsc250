class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make   # Initialize vehicle make
        self.value = vehicle_value  # Initialize vehicle value

    def display_info(self):
        print(f"Vehicle Make: {self.make}")  # Display vehicle make
        print(f"Value: {self.value}")        # Display vehicle value

#Used the Help of Github CoPilot and ChatGPT
class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)  # Call parent constructor with make and value
        self.model = car_model                 # Initialize car model
        self.year = car_year                   # Initialize car year

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.model}")  # Display car details
        print(f"Value: {self.value}")                                # Display car value

#Used the Help of Github CoPilot and ChatGPT
class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)  # Call parent constructor with make and value
        self.model = truck_model                   # Initialize truck model
        self.year = truck_year                     # Initialize truck year
        self.all_wheel_drive = is_allwd            # Initialize whether truck is all-wheel drive

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.model}")   # Display truck details
        print(f"Value: {self.value}")                                 # Display truck value
        print(f"All Wheel Drive: {self.all_wheel_drive}")             # Display all-wheel drive status


def display_list(my_collection):
    for i, vehicle in enumerate(my_collection, start=1):
        print(f"Vehicle {i} Information:")  # Display vehicle number
        vehicle.display_info()              # Call the display_info method of the vehicle
        print()                             # Print a blank line after each vehicle's info

#Used the Help of Github CoPilot and ChatGPT
if __name__ == "__main__":
    my_collection = []  # Initialize an empty list to store vehicles

    while True:
        user_string = input().strip()  # Take user input and remove any leading/trailing whitespace
        if user_string == "done":      # If input is "done", stop input collection
            break

        details = user_string.split()  # Split input into parts
        vehicle_type = details[0]      # First part determines the type of vehicle

        if vehicle_type == "vehicle":
            make = details[1]                # Extract vehicle make
            value = int(details[2])          # Extract vehicle value and convert to integer
            vehicle = Vehicle(make, value)   # Create Vehicle object
            my_collection.append(vehicle)    # Add Vehicle object to collection

        elif vehicle_type == "car":
            make = details[1]                # Extract car make
            value = int(details[2])          # Extract car value and convert to integer
            model = details[3]               # Extract car model
            year = int(details[4])           # Extract car year and convert to integer
            car = Car(make, value, model, year)  # Create Car object
            my_collection.append(car)        # Add Car object to collection

        elif vehicle_type == "truck":
            make = details[1]                # Extract truck make
            value = int(details[2])          # Extract truck value and convert to integer
            model = details[3]               # Extract truck model
            year = int(details[4])           # Extract truck year and convert to integer
            all_wheel_drive = details[5].lower() == "true"  # Determine if truck is all-wheel drive
            truck = Truck(make, value, model, year, all_wheel_drive)  # Create Truck object
            my_collection.append(truck)      # Add Truck object to collection

    display_list(my_collection)  # Call function to display information for all vehicles in collection
