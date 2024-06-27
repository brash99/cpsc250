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
       super().__init__(car_make, car_value)
       self.car_model = car_model
       self.car_year = car_year


    def display_info(self):
        print(f'   Description: {self.car_year} { self.vehicle_make} {self.car_model} ')
        print(f'   Value: {self.vehicle_value}')


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd



    def display_info(self):
        print(f'   Description: {self.truck_year} {self.vehicle_make} {self.truck_model}')
        print(f'   Value: {self.vehicle_value}')
        print(f'   All Wheel Drive: {self.is_allwd}')


# TODO:  Define the display_list() function

def display_list(collection):
    for i, vehicle in enumerate(collection):
        print(f'Vehicle {i+1} Information: ')
        collection[i].display_info()
        print()


if __name__ == "__main__":

    # TODO: Declare a list called my_collection

    user_string = input()
    my_collection = []

    while user_string != 'done':
        tokens = user_string.split()
        vehicle_type = tokens[0]
        vehicle_make = tokens[1]
        vehicle_value = tokens[2]
        if vehicle_type == 'vehicle':
            my_vehicle = Vehicle(vehicle_make, vehicle_value)
            my_collection.append(my_vehicle)
        elif vehicle_type == 'car':
            car_model = tokens[3]
            car_year = int(tokens[4])
            my_car = Car(vehicle_make, vehicle_value, car_model, car_year)
            my_collection.append(my_car)
        elif vehicle_type == 'truck':
            truck_model = tokens[3]
            truck_year = int(tokens[4])
            is_allwd = tokens[5]
            my_truck = Truck(vehicle_make, vehicle_value, truck_model, truck_year, is_allwd)
            my_collection.append(my_truck)

        user_string = input()

    # TODO: Call the display_list() function
    display_list(my_collection)

#refrenced the flower/plant file