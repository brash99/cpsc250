# Define the base Vehicle class
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make  # Vehicle Make
        self.vehicle_value = vehicle_value  # Value of Vehicle

    def display_info(self):
        # Returns a string with vehicle info
        return f"Vehicle Make: {self.vehicle_make}\nValue: {self.vehicle_value}"

# Define the Car class, derived from Vehicle
class Car(Vehicle):
    def __init__(self, vehicle_make, vehicle_value, car_model, car_year):
        super().__init__(vehicle_make, vehicle_value)  # Init base attributes
        self.car_model = car_model  # Car Model
        self.car_year = car_year  # Car Year

    def display_info(self):
        return f"Description: {self.car_year} {self.vehicle_make} {self.car_model}\nValue: {self.vehicle_value}"

# Define the Truck class, derived from Vehicle
class Truck(Vehicle):
    def __init__(self, vehicle_make, vehicle_value, truck_model, truck_year, is_allwd):
        super().__init__(vehicle_make, vehicle_value)  # Init base attributes
        self.truck_model = truck_model  # Truck Model
        self.truck_year = truck_year  # Truck Year
        self.is_allwd = is_allwd  # All Wheel Drive Status

    def display_info(self):
        return f"Description: {self.truck_year} {self.vehicle_make} {self.truck_model}\nValue: {self.vehicle_value}\nAll Wheel Drive: {self.is_allwd}"

# Function to display information of all vehicles in the collection
def display_list(collection):
    for i, vehicle in enumerate(collection):
        print(f"Vehicle {i + 1} Information:")
        print(vehicle.display_info())
        print()  # Add a blank line for better readability

# Entry point of the program
if __name__ == "__main__":
    # Declare a list called my_collection
    # Chatgpt partially gor this portion and display_list
    my_collection = []

    print("Enter the vehicle info, or 'done' to quit:")
    user_string = input()

    while user_string != 'done':
        parts = user_string.split()  # Split the user_string input into variables

        # Check if input is a vehicle, car, or truck
        if len(parts) == 3 and parts[0].lower() == 'vehicle':
            _, make, value = parts
            value = int(value)
            my_collection.append(Vehicle(make, value))
        elif len(parts) == 5 and parts[0].lower() == 'car':
            _, make, value, model, year = parts
            value = int(value)
            year = int(year)
            my_collection.append(Car(make, value, model, year))
        elif len(parts) == 6 and parts[0].lower() == 'truck':
            _, make, value, model, year, all_wheel_drive = parts
            value = int(value)
            year = int(year)
            all_wheel_drive = all_wheel_drive.lower() == 'true'
            my_collection.append(Truck(make, value, model, year, all_wheel_drive))
        else:
            print("Invalid input. Please enter data in the correct format.")

        user_string = input()

    # Call the display_list() function
    display_list(my_collection)


