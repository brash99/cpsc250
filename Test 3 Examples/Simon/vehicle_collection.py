class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = int(vehicle_value)  # Convert value to integer

    def display_info(self):
        print(f"\tVehicle Make: {self.vehicle_make}")
        print(f"\tValue: {self.vehicle_value}\n")


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)
        self.car_model = car_model
        self.car_year = car_year

    def display_info(self):
        print(f"\tDescription: {self.car_year} {self.vehicle_make} {self.car_model}")
        print(f"\tValue: {self.vehicle_value}\n")


class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

    def display_info(self):
        print(f"\tDescription: {self.truck_year} {self.vehicle_make} {self.truck_model}")
        print(f"\tValue: {self.vehicle_value}")
        print(f"\tAll Wheel Drive: {self.is_allwd}\n")


def display_list(collection):
    for idx, vehicle in enumerate(collection, start=1):
        print(f"Vehicle {idx} Information:")
        vehicle.display_info()


if __name__ == "__main__":
    my_collection = []

    while True:
        user_input = input("Enter vehicle details (make, value, model, year, [allwd]) or 'done' to finish: ")

        if user_input.lower() == 'done':
            break

        # Splitting input and determining vehicle type
        data = user_input.split()
        vehicle_type = data[0].lower()  # First word determines type

        if vehicle_type == 'vehicle':
            make, value = data[1], int(data[2])  # Convert value to integer
            vehicle = Vehicle(make, value)
        elif vehicle_type == 'car':
            make, value, model, year = data[1], int(data[2]), data[3], int(data[4])
            vehicle = Car(make, value, model, year)
        elif vehicle_type == 'truck':
            make, value, model, year = data[1], int(data[2]), data[3], int(data[4])
            is_allwd = True if len(data) > 5 and data[5].lower() == 'true' else False
            vehicle = Truck(make, value, model, year, is_allwd)
        else:
            print("Invalid vehicle type")
            continue

        my_collection.append(vehicle)

    display_list(my_collection)
