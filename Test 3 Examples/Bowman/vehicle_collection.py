class Vehicle:
    def __init__(self, make, value):
        # init Vehicle class with make and value
        self.make = make
        self.value = value

    def print_info(self):
        # print the info of the vehicle like make and value
        print(f"Vehicle Make: {self.make}")
        print(f"Value: {self.value}")


class Car(Vehicle):
    def __init__(self, make, value, model, year):
        # init the Car class by inheriting from Vehicle function above and adding model and year
        super().__init__(make, value)
        self.model = model
        self.year = year

    def print_info(self):
        # print the info of the vehicle like make, year, model, and value
        print(f"Description: {self.year} {self.make} {self.model}")
        print(f"Value: {self.value}")


class Truck(Vehicle):
    def __init__(self, make, value, model, year, all_wheel_drive):
        # init the Truck class by inheriting from Vehicle function and adding model, year, plus all_wheel_drive
        super().__init__(make, value)
        self.model = model
        self.year = year
        self.all_wheel_drive = all_wheel_drive

    def print_info(self):
        # print the info of the vehicle like make, year, model, and value along with whether it has all-wheel drive
        print(f"Description: {self.year} {self.make} {self.model}")
        print(f"Value: {self.value}")
        print(f"All Wheel Drive: {str(self.all_wheel_drive).lower()}")


def print_list(my_collection):
    # for each vehicle this function will prints its index and calls the print_info method to print its info
    for i, vehicle in enumerate(my_collection):
        print(f"Vehicle {i + 1} Information:")
        vehicle.print_info()


if __name__ == "__main__":
    # create an empty list to hold the objects of the vehicles
    my_collection = []

    # read input until "done" is entered by using the while loop
    while True:
        user_input = input()
        if user_input == 'done':
            break

        # this will split the input into parts to show all the info of the vehicles
        input_split = user_input.split()

        # input for the vehicle
        if input_split[0] == 'vehicle':
            make = input_split[1]
            value = int(input_split[2])
            # make a Vehicle object and add it
            my_collection.append(Vehicle(make, value))

        # input for the car
        elif input_split[0] == 'car':
            make = input_split[1]
            value = int(input_split[2])
            model = input_split[3]
            year = int(input_split[4])
            # make a car object and add it
            my_collection.append(Car(make, value, model, year))

        # input for the truck
        elif input_split[0] == 'truck':
            make = input_split[1]
            value = int(input_split[2])
            model = input_split[3]
            year = int(input_split[4])
            all_wheel_drive = input_split[5].lower() == 'true'
            # make a truck object and add it
            my_collection.append(Truck(make, value, model, year, all_wheel_drive))

    # print out all the info about the vehicles by calling the print_list function
    print_list(my_collection)
