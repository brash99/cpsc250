class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.make = vehicle_make
        self.value = vehicle_value

    def display_info(self):
        print('Vehicle Make:', self.make)
        print('Value:', self.value)


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.model = car_model
        self.year = car_year

    def display_info(self):
        print(f'Description: {self.year} {self.make} {self.model}')
        print('Value:', self.value)


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_all_wd):
        super().__init__(truck_make, truck_value)
        self.model = truck_model
        self.year = truck_year
        self.is_all_wd = is_all_wd

    def display_info(self):
        print(f'Description: {self.year} {self.make} {self.model}')
        print('Value:', self.value)
        print('All Wheel Drive:', self.is_all_wd)


def display_list(collection):
    for index, vehicle in enumerate(collection):
        print(f'Vehicle {index + 1} Information:')
        vehicle.display_info()
        print()


if __name__ == "__main__":
    my_collection = []

    print("Enter vehicle information (type 'done' to finish):")
    while True:
        user_string = input()
        if user_string == 'done':
            break
# Used ChatGPT for this part
        data = user_string.split()
        if data[0] == 'vehicle':
            make = data[1]
            value = int(data[2])
            my_collection.append(Vehicle(make, value))
        elif data[0] == 'car':
            make = data[1]
            value = int(data[2])
            model = data[3]
            year = int(data[4])
            my_collection.append(Car(make, value, model, year))
        elif data[0] == 'truck':
            make = data[1]
            value = int(data[2])
            model = data[3]
            year = int(data[4])
            is_all_wd = data[5].lower() == 'true'
            my_collection.append(Truck(make, value, model, year, is_all_wd))

    display_list(my_collection)

