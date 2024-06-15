FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.gas_tank = FULL_TANK
        self.make = make

    # Return car model
    def get_model(self):
        # Update the return statment.

        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.

        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.

        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.

        return self.gas_tank

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if not self.engine_on:
            print('Engine is off. Please start the engine first.')
        if miles_to_drive > 0:
            max_distance = self.gas_tank * self.mpg
            if miles_to_drive <= max_distance:
                self.odometer += miles_to_drive
                self.gas_tank -= miles_to_drive / self.mpg
            else:
                self.odometer += max_distance
                self.gas_tank = 0.0
                self.engine_on = False



    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
            if self.engine_on:
                print("Cannot add gas while the engine is on. Please turn off the engine first.")
                return

            if amount_to_add > 0:
                self.gas_tank = min(FULL_TANK, self.gas_tank + amount_to_add)

        # Type your code here and remove the return statement



    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True
    def stop_engine(self):
        # Type your code here and remove the return statement
        self.engine_on = False


if __name__ == "__main__":
    car = FancyCar("Honda Civic", 30.0)
    car.start_engine()
    car.honk_horn()
    car.drive(100)
    print(f"Odometer: {car.check_odometer()} miles")
    print(f"Gas gauge: {car.check_gas_gauge()} gallons")
    car.stop_engine()
    car.add_gas(5)
    print(f"Gas gauge after refilling: {car.check_gas_gauge()} gallons")