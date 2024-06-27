class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make
        self.value = vehicle_value

    def display_info(self, index):
        print(f'Vehicle {index} Information:')
        print(f'    Vehicle Make: {self.make}')
        print(f'    Vehicle Value: {self.value}')


class Car(Vehicle):
    def __init__(self, vehicle_make, vehicle_value, car_model, car_year):
        super().__init__(vehicle_make, vehicle_value)
        self.model = car_model
        self.year = car_year

    def display_info(self, index):
        print(f'    Description:{self.year} {self.make} {self.model} ')
        print(f'    Value: {self.value}')



class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.model = truck_model
        self.year = truck_year
        self.is_allwd = 'True' if is_allwd else 'False'

    def display_info(self, index):
        print(f'    Description: {self.make} {self.model} {self.year}')
        print(f'    Value: {self.value}')
        print(f'    All-Wheel Drive: {self.is_allwd}')


def display_list(collection):
    for i, vehicle in enumerate(collection, start=1):
        vehicle.display_info(i)
        print()


if __name__ == "__main__":
    my_collection = []

    user_input = input().strip()

    while user_input != 'done':
        type_vehicle, *args = user_input.split()

        if type_vehicle == 'vehicle':
            vehicle_make = args[0]
            vehicle_value = (args[1])
            vehicle = Vehicle(vehicle_make, vehicle_value)
            my_collection.append(vehicle)
        elif type_vehicle == 'car':
            car_make = args[0]
            car_value = (args[1])
            car_model = args[2]
            car_year = int(args[3])
            car = Car(car_make, car_value, car_model, car_year)
            my_collection.append(car)
        elif type_vehicle == 'truck':
            truck_make = args[0]
            truck_value = (args[1])
            truck_model = args[2]
            truck_year = int(args[3])
            is_allwd = args[4].lower() == 'true'  # Convert string to boolean
            truck = Truck(truck_make, truck_value, truck_model, truck_year, is_allwd)
            my_collection.append(truck)

        user_input = input().strip()

    display_list(my_collection)
