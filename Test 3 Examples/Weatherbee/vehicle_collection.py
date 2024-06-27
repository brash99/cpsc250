class Vehicle:
    def __init__(self, make, value):
        self.make = make
        self.value = value

    def display_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Value: {self.value}")


class Car(Vehicle):
    def __init__(self, make, value, model, year):
        super().__init__(make, value)
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.model}")
        print(f"Value: {self.value}")


class Truck(Vehicle):
    def __init__(self, make, value, model, year, all_wheel_drive):
        super().__init__(make, value)
        self.model = model
        self.year = year
        self.all_wheel_drive = all_wheel_drive

    def display_info(self):
        print(f"Description: {self.year} {self.make} {self.model}")
        print(f"Value: {self.value}")
        print(f"All Wheel Drive: {self.all_wheel_drive}")


def display_list(collection):
    for i, vehicle in enumerate(collection):
        print(f"Vehicle {i + 1} Information:")
        vehicle.display_info()
        print()  # Print a blank line for separation


def main():
    my_collection = []
    predefined_input = [
        "vehicle Vespa 7800",
        "car Chevrolet 27000 BelAir 1957",
        "truck Fargo 22500 Pickup 1948 false",
        "vehicle Scooter 200",
        "done"
    ]

    for user_input in predefined_input:
        user_input = user_input.strip()
        if user_input == 'done':
            break
        parts = user_input.split()
        if parts[0] == 'vehicle':
            _, make, value = parts
            value = int(value)
            my_collection.append(Vehicle(make, value))
        elif parts[0] == 'car':
            _, make, value, model, year = parts
            value = int(value)
            year = int(year)
            my_collection.append(Car(make, value, model, year))
        elif parts[0] == 'truck':
            _, make, value, model, year, all_wheel_drive = parts
            value = int(value)
            year = int(year)
            all_wheel_drive = all_wheel_drive.lower() == 'true'
            my_collection.append(Truck(make, value, model, year, all_wheel_drive))

    display_list(my_collection)


if __name__ == "__main__":
    main()
