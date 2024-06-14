# Define the global variable FULL_TANK
FULL_TANK = 14.0


class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0, odometer=5, fuel=FULL_TANK):
        # Initialize the instance variables with user-provided values or defaults
        self.make = make  # Car model
        self.mpg = mpg  # Miles per gallon
        self.odometer = odometer  # Initial odometer reading
        self.engine_on = False  # Engine status
        self.fuel = fuel  # Initial fuel amount in the gas tank

    # Method to check the odometer
    def check_odometer(self):
        return self.odometer

    # Method to check the gas gauge
    def check_gas_gauge(self):
        return self.fuel

    # Method to get the model
    def get_model(self):
        return self.make

    # Method to get the miles per gallon
    def get_mpg(self):
        return self.mpg

    # Method to honk the horn
    def honk_horn(self):
        return f"The {self.make} says beep beep!"
        #print(f"The {self.make} says beep beep!")

    # Method to drive the car
    def drive(self, miles_to_drive):
        if miles_to_drive > 0 and self.engine_on:
            fuel_needed = miles_to_drive / self.mpg
            if fuel_needed <= self.fuel:
                self.odometer += miles_to_drive
                self.fuel -= fuel_needed
            else:
                self.odometer += self.fuel * self.mpg
                self.fuel = 0
                self.engine_on = False

    # Method to add gas to the tank
    def add_gas(self, amount):
        if amount > 0 and not self.engine_on:
            self.fuel = min(FULL_TANK, self.fuel + amount)

    # Method to start the engine
    def start_engine(self):
        self.engine_on = True

    # Method to stop the engine
    def stop_engine(self):
        self.engine_on = False


# Sample testing code
if __name__ == "__main__":
    # Create a FancyCar object with user inputs
    model = input("Enter the car model: ")
    mpg = float(input("Enter the miles per gallon (MPG): "))
    odometer = int(input("Enter the initial odometer reading: "))
    fuel = float(input("Enter the initial amount of fuel in the tank: "))

    car = FancyCar(model, mpg, odometer, fuel)

    # Test the class methods
    print(f"Model: {car.get_model()}")  # User-provided model
    print(f"MPG: {car.get_mpg()}")  # User-provided MPG
    print(f"Odometer: {car.check_odometer()}")  # User-provided odometer reading
    print(f"Fuel: {car.check_gas_gauge()}")  # User-provided fuel amount
    print(f"Engine status: {car.engine_on}")  # Should be False

    # Test other functionalities
    car.start_engine()
    print(f"Engine status after starting: {car.engine_on}")  # Should be True

    car.drive(10)
    print(f"Odometer after driving 10 miles: {car.check_odometer()}")  # Should increase
    print(f"Fuel after driving 10 miles: {car.check_gas_gauge()}")  # Should decrease

    car.stop_engine()
    print(f"Engine status after stopping: {car.engine_on}")  # Should be False

    car.add_gas(5)
    print(f"Fuel after adding 5 gallons: {car.check_gas_gauge()}")  # Should increase but not exceed FULL_TANK

    print(car.honk_horn())  # Should honk with the user-provided model
