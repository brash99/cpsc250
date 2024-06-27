# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    #defining and initializing atributes of vehicle
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value
    #printing vehicle information
    def display_info(self):
        print(f'Vehicle Make: {self.vehicle_make}')
        print(f'Value: {self.vehicle_value}')


class Car(Vehicle):
    #defining and initializing atributes of car vehicle
    def __init__(self, car_make, car_value, car_model, car_year):
        self.car_make = car_make
        self.car_value = car_value
        self.car_model = car_model
        self.car_year = car_year
    #printing car vehicle information
    def display_info(self):
        print(f'Description: {self.car_year} {self.car_make} {self.car_model}')
        print(f'Value: {self.car_value}')

class Truck(Vehicle):
    #defining and initializing atributes of truck vehicle
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        self.truck_make = truck_make
        self.truck_value = truck_value
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd
    #printing truck vehicle information
    def display_info(self):
        print(f'Description: {self.truck_year} {self.truck_make} {self.truck_model}')
        print(f'Value: {self.truck_value}')
        print(f'All Wheel Drive: {self.is_allwd}')
#printing each vehicle starting at 1 using my_collection and adding an empty line bewteen each vehicle
def display_list(collection):
    for index, vehicle in enumerate(collection, start=1):
        print(f'Vehicle {index} Information:')
        vehicle.display_info()
        print()

if __name__ == "__main__":
    my_collection = []
    # TODO: Declare a list called my_collection

    user_string = input()

    while user_string != 'done':
        user_string_split = user_string.split()
        #assinging vehicle attributs with input parts when the first part of the input is vehicle and adding it to my_collection
        if user_string_split[0] == 'vehicle':
            vehicle_make = user_string_split[1]
            vehicle_value = int(user_string_split[2])
            my_collection.append(Vehicle(vehicle_make, vehicle_value))
        #assinging car attributs with input parts when the first part of the input is car and adding it to my_collection
        elif user_string_split[0] == 'car':
            car_make = user_string_split[1]
            car_value = int(user_string_split[2])
            car_model = user_string_split[3]
            car_year = int(user_string_split[4])
            my_collection.append(Car(car_make, car_value, car_model, car_year))
        #assinging truck attributs with input parts when the first part of the input is truck and adding it to my_collection
        elif user_string_split[0] == 'truck':
            truck_make = user_string_split[1]
            truck_value = int(user_string_split[2])
            truck_model = user_string_split[3]
            truck_year = int(user_string_split[4])
            is_allwd = user_string_split[5]
            my_collection.append(Truck(truck_make, truck_value, truck_model, truck_year, is_allwd))

        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        user_string = input()
    #outputing each input vehicles informtion
    display_list(my_collection)

    # TODO: Call the display_list() function
