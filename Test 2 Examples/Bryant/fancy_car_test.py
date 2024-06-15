# Define a global variable for FULL_TANK
FULL_TANK = 14.0

class FancyCar:
    def __init__(self, model="Old Clunker", mpg=24.0):
        self.model = model
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.fuel = FULL_TANK

    # Step 1: Instance methods to check the odometer, check the gas gauge, get the model, and get the miles per gallon
    def check_odometer(self):
        return self.odometer

    def check_gas_gauge(self):
        return self.fuel

    def get_model(self):
        return self.model

    def get_mpg(self):
        return self.mpg

    # Step 2: Instance method to honk horn
    def honk_horn(self):
        print(f"The {self.model} says beep beep!")

    # Step 3: Instance method to drive
    def drive(self, miles_to_drive):
        if self.engine_on and miles_to_drive > 0:
            max_drivable_distance = self.fuel * self.mpg
            if miles_to_drive <= max_drivable_distance:
                self.odometer += miles_to_drive
                self.fuel -= miles_to_drive / self.mpg
            else:
                self.odometer += max_drivable_distance
                self.fuel = 0
                self.engine_on = False

    # Step 4: Instance method to add gas
    def add_gas(self, amount):
        if not self.engine_on and amount > 0:
            self.fuel = min(self.fuel + amount, FULL_TANK)

    # Step 6: Instance methods to start and stop the engine
    def start_engine(self):
        self.engine_on = True

    def stop_engine(self):
        self.engine_on = False

# Test the FancyCar class
def main():
    car = FancyCar("Honda Civic", 30.0)
    car.start_engine()
    print(f"Odometer={car.check_odometer()} miles")
    print(f"Gas_tank={car.check_gas_gauge()} gallons")
    car.honk_horn()
    car.drive(100)
    print(f"Odometer after driving 100 miles: {car.check_odometer()} miles")
    print(f"Gas gauge after driving 100 miles:{car.check_gas_gauge()} gallons")
    car.add_gas(5)
    print(f"Gas gauge after adding 5 gallons: {car.check_gas_gauge()} gallons")
    car.stop_engine()
    car.add_gas(5)
    print(f"Gas gauge after adding another 5 gallons with engine off: {car.check_gas_gauge()} gallons")

if __name__ == "__main__":
    main()