# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    #format
    def display_info(self):
        print(f"    Vehicle Make: {self.vehicle_make}")
        print(f"    Value: {self.vehicle_value}\n")




class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
# super(). function pulls info from super class and lets me add to it to aviod re-wrting code
        super().__init__(car_make, car_value)
        self.car_make = car_make
        self.car_value = car_value
        self.car_model = car_model
        self.car_year = car_year

    # format
    def display_info(self):
        print(f'    Description: {self.car_year} {self.car_make} {self.car_model}')
        print(f"    Value: {self.vehicle_value}\n")

class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_make = truck_make
        self.truck_value = truck_value
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

    # format
    def display_info(self):
        print(f"    Description: {self.truck_year} {self.vehicle_make} {self.truck_model}")
        print(f"    Value: {self.vehicle_value}")
        print(f"    All Wheel Drive: {self.is_allwd}\n")

#this information sets up the numbers of vehicles I have iterated through vehicle 1 .... vehicle 2 ... ,etc
# refrece from stackover flow
# could have used enumerate function but thats to scary since i am unformiliar with it
def display_list(my_collection):
    x = 1
    for vehicle in my_collection:
        print(f"Vehicle {x} Information:")
        vehicle.display_info()
        x += 1


# TODO:  Define the display_list() function

if __name__ == "__main__":
    my_collection = []
    # TODO: Declare a list called my_collection

    user_string = input('Add Input')
#done ends the code
    while user_string != 'done':
        user_data = user_string.split()        #splits input in to a list of strings ex. ABC --> ['A', 'B', 'C']
        # identifys this is a vehicle and sends info to the vehicle class
        if user_data[0] == 'vehicle':
            vehicle = Vehicle(user_data[1], user_data[2]) # sends information to the class
            my_collection.append(vehicle)
        ##identifys this is a car and sends info to the car class
        elif user_data[0] == 'car':
            car = Car(user_data[1], user_data[2], user_data[3], user_data[4])
            my_collection.append(car)
        #truck info Truck class
        elif user_data[0] == 'truck':
            truck = Truck(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
            my_collection.append(truck)
        #my_collection.append sends all info fromcalss to  my_collection to pring
        user_string = input('Add Input')
    #give user the ability to add another input ORRR say done and end code then display
    display_list(my_collection)
        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection


    # TODO: Call the display_list() function
