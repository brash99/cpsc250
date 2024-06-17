FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        self.make = make
        self.mpg = mpg
        self.odometer = 0
        self.engine_on = False
        self.fuel_in_tank = FULL_TANK


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

        return self.fuel_in_tank

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        if self.engine_on and miles_to_drive > 0:
            max_distance = self.fuel_in_tank * self.mpg
            if miles_to_drive <= max_distance:
                self.odometer += miles_to_drive
                self.fuel_in_tank -= miles_to_drive / self.mpg
            else:
                self.odometer += max_distance
                self.fuel_in_tank = 0.0
                print(f'Out of gas! Only drove {max_distance} miles.')
                self.stop_engine()
        else:
            print('Engine is not on or invalid miles to drive.')


    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        if not self.engine_on and amount_to_add > 0:
            self.fuel_in_tank = min(self.fuel_in_tank + amount_to_add, self.FULL_TANK)
        else:
            print('Engine must be off and amount must be positive.')

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        self.engine_on = False