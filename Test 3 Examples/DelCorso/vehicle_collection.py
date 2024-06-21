# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make
        self.value = vehicle_value
        #the variables used in the class

    def display_info(self):
        return f"Vehicle Make: {self.make} \nValue: {self.value}"
    #returns a string of the make and value of the car


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(vehicle_make, vehicle_value)
        #calls the inside class vehicle
        self.model = car_model
        self.year = car_year
        #more variables added


    def display_info(self):
        return f"Description: {self.year} {self.make} {self.model}\nValue: {self.value}"
    #The car description string that has year, make, and model


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(make, value)
        self.model = truck_model
        self.year = truck_year
        self.is_allwd = is_allwd
        #calls the inside class and inputs different truck variables.

    def display_info(self):
        return f"Description: {self.year} {self.make} {self.model}\nValue: {self.value}\nAll Wheel Drive: {self.is_allwd}"
    # gives description of the truck.
    
    
# TODO:  Define the display_list() function
def display_list(my_collection):
    for i, vehicle in enumerate(my_collection, start=1):
        print(f"Vehicle {i} Information:\n{vehicle.display_info()}\n")
        #my_collection is a list of Vehicle, Car, Truck class,
        # the for loop goes through every vehicle and start 1 starts at 1 not 0.
        #the {vehicle.display_info()} is replaced by the info of the vehicle, which you get by calling the display_info() method of the Vehicle, Car, or Truck class.


if __name__ == "__main__":

    # TODO: Declare a list called my_collection
    my_collection = []
    #da list of vehicles, cars, and trucks.
    user_string = input()
    
    while user_string != 'done':
        data = user_string.split()
        if data[0] == 'vehicle':
            my_collection.append(Vehicle(data[1], int(data[2])))
            # is it a vehicle if so give this info.
        elif data[0] == 'car':
            my_collection.append(Car(data[1], int(data[2]), data[3], int(data[4])))
            # is it a car if so give this info.
        elif data[0] == 'truck':
            my_collection.append(Truck(data[1], int(data[2]), data[3], int(data[4]), data[5] == 'true'))
            # is it a truck if so give this info all to the list.

        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection

        user_string = input()
    display_list(my_collection)

    # TODO: Call the display_list() function
