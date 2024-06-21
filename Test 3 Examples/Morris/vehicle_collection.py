# Define the base Vehicle class
class Vehicle:
    def __init__(self, make, value):
        self.make = make
        self.value = value

    def display_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Value: {self.value}")


# Define the Car class derived from Vehicle
class Car(Vehicle):
    def __init__(self, make, value, description, year):
        super().__init__(make, value)
        self.description = description
        self.year = year

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.description}")
        print(f"Value: {self.value}")


# Define the Truck class derived from Vehicle
class Truck(Vehicle):
    def __init__(self, make, value, description, year, all_wheel_drive):
        super().__init__(make, value)
        self.description = description
        self.year = year
        self.all_wheel_drive = all_wheel_drive

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.description}")
        print(f"Value: {self.value}")
        print(f"All Wheel Drive: {self.all_wheel_drive}")


# Step 2: Create a list called my_collection
my_collection = []


# Step 3: Read input data and store objects in my_collection
def read_input():
    global my_collection  # Declare my_collection as global to modify it inside the function
    while True:
        data = input()
        if data == "done":
            break
        parts = data.split()
        vehicle_type = parts[0]

        if vehicle_type == "vehicle":
            make = parts[1]
            value = int(parts[2])
            my_collection.append(Vehicle(make, value))

        elif vehicle_type == "car":
            make = parts[1]
            value = int(parts[2])
            description = parts[3]
            year = int(parts[4])
            my_collection.append(Car(make, value, description, year))

        elif vehicle_type == "truck":
            make = parts[1]
            value = int(parts[2])
            description = parts[3]
            year = int(parts[4])
            all_wheel_drive = parts[5].lower() == 'true'
            my_collection.append(Truck(make, value, description, year, all_wheel_drive))


# Step 4: Define the display_list function
def display_list():
    for index, vehicle in enumerate(my_collection, start=1):
        print(f"Vehicle {index} Information:")
        vehicle.display_info()
        print()  # Add an empty line between vehicles for better readability


# Main function to run the program
if __name__ == "__main__":
    read_input()
    display_list()
