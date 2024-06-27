# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make #initialize the vehicle make
        self.value = vehicle_value #initialzie the vehicle value



    def display_info(self):
        print(f"Vehicle Make: {self.make}") #printing vehicle make
        print(f"Vehicle Value: {self.value}") #printing vehicle value


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        self.vehicle_make = car_make #initialize the car make
        self.value = car_value #initialize the car value
        self.model = car_model #initialize the car model
        self.year = car_year #initialize the car year

    def display_info(self):
        print(f"Vehicle Make: {self.vehicle_make}") #printing the car make
        print(f"Vehicle Value: {self.value}") #printing the car value
        print(f"Car Model: {self.model}") #printing the car model
        print(f"Car Year: {self.year}") #printing the car year

class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        self.vehicle_make = truck_make #initialize the truck make
        self.vehicle_value = truck_value #initialize the truck value
        self.truckmodel = truck_model #initialize the truck model
        self.truckyear = truck_year#initialize the truck year
        self.allwd = is_allwd #initialize if its all wheel drive

    def display_info(self):
        print(f"Vehicle Make: {self.vehicle_make}") #printing the truck make
        print(f"Vehicle Value: {self.vehicle_value}") #printing the truck value
        print(f"Truck Model: {self.truckmodel}") #printing the truck model
        print(f"Truck Year: {self.truckyear}") #printing the truck year
        print(f"Is All-Wheel Drive: {self.allwd}") #printing if its all wheel drive

# TODO:  Define the display_list() function
def display_list(my_collection):
    for i, vehicle in enumerate(my_collection, start=1):
        print(f"Vehicle {i} Information:") #printing the vehicle number
        vehicle.display_info()
        print()


if __name__ == "__main__":

    # TODO: Declare a list called my_collection
    my_collection = []
    while True:
        user_string = input() #input
        if user_string == 'done':
            break
        elif user_string.startswith("vehicle"):
            _, vehicle_make, vehicle_value = user_string.split()
            my_collection.append(Vehicle(vehicle_make, vehicle_value)) #adding to the list
        elif user_string.startswith("car"): #if the string wants a car
            _, car_make, car_value, car_model, car_year = user_string.split()
            my_collection.append(Car(car_make, car_value, car_model, car_year))
        elif user_string.startswith("truck"): #if the string wants a truck
            _, truck_make, truck_value, truck_model, truck_year, is_allwd = user_string.split()
            my_collection.append(Truck(truck_make, truck_value, truck_model, truck_year, is_allwd == "true")) #adding to the list

    display_list(my_collection) #output

        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection

    # TODO: Call the display_list() function
