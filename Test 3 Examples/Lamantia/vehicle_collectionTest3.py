# TODO:  write the __init__ and display_info functions for the classes
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value

#Defined display info for vehicle make and value
    def display_info(self):
        print('Vehicle Information:')
        print(f'Vehicle Make: {self.vehicle_make}')
        print(f'Value: {self.vehicle_value}')


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.car_model = car_model
        self.car_year = car_year

#Defined display info for make, value, model, and year
    def display_info(self):
        print('Vehicle Information:')
        print(f'Description: {self.car_year} {self.vehicle_make} {self.car_model}')
        print(f'Value: {self.vehicle_value}')

#Defined Truck class
class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

#Defined display info for truck
    def display_info(self):
        print('Vehicle Information:')
        print(f'Description: {self.truck_year} {self.vehicle_make} {self.truck_model}')
        print(f'Value: {self.vehicle_value}')
        print(f'All Wheel Drive: {self.is_allwd}')

#Defined the display_list() function
def display_list(vehicle_list):
    for vehicle in vehicle_list:
        vehicle.display_info()
        print()

if __name__ == "__main__":

    #Declared a list called my_collection
    my_collection = []

    user_string = input()

    while user_string != 'done':  #Ending with done
        details = user_string.split()

        if details[0].lower() == 'vehicle' and len(details) == 3:
            vehicle = Vehicle(details[1], details[2])
            my_collection.append(vehicle)
        elif details[0].lower() == 'car' and len(details) == 5:
            car = Car(details[1], details[2], details[3], details[4])
            my_collection.append(car)
        elif details[0].lower() == 'truck' and len(details) == 6:
            truck = Truck(details[1], details[2], details[3], details[4], details[5])
            my_collection.append(truck)

        user_string = input()

    #Created the display_list() function

    display_list(my_collection)
