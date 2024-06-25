# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

    def display_info(self):
        print(f'   Vehicle Make: {self.vehicle_make}')
        print(f'   Value: {self.vehicle_value}')


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        Vehicle.__init__(self, car_make, car_value) #Zybooks credit, i forgot to initialize w parent class
        self.car_make = car_make
        self.car_value = car_value
        self.car_model = car_model
        self.car_year = car_year


    def display_info(self):
        print(f'   Description: {self.car_year} {self.car_make} {self.car_model}')
        print(f'   Value: {self.car_value}')


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        Vehicle.__init__(self, truck_make, truck_value) #Zybooks credit, i forgot to initialize w parent class
        self.truck_make = truck_make
        self.truck_value = truck_value
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd


    def display_info(self):
        print(f'   Description: {self.truck_year} {self.truck_make} {self.truck_model}')
        print(f'   Value: {self.truck_value}')
        print(f'   All Wheel Drive: {self.is_allwd}')
    
def display_list(collection):
    for i in range(len(collection)): #lines 42-44 from Zybooks 13.11.1
        print(f'Vehicle {i + 1}: Information:')
        collection[i].display_info()
# TODO:  Define the display_list() function

if __name__ == "__main__":

    my_collection = []
    # TODO: Declare a list called my_collection

    user_string = input()
    
    while user_string != 'done':
        user_string = user_string.split()

#the idea to rename things into my_vehcile was Zybooks idea, but using the indexes with the original user_string
#was my idea. So lines 60, 64, 68 were zybooks
        if user_string[0] == 'vehicle':
            my_vehicle = Vehicle(user_string[1], user_string[2])
            my_collection.append(my_vehicle)

        elif user_string[0] == 'car':
            my_car = Car(user_string[1], user_string[2], user_string[3], user_string[4])
            my_collection.append(my_car)

        elif user_string[0] == 'truck':
            my_truck = Truck(user_string[1], user_string[2], user_string[3], user_string[4], user_string[5])
            my_collection.append(my_truck)


        # TODO: Check if input is a vehicle, car, or truck
        #       Split the user_string input into variables
        #       Store as an object of the appropriate type
        #       Add to the list my_collection
        user_string = input()

display_list(my_collection)

    # TODO: Call the display_list() function
