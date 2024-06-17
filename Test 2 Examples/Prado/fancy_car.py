FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.fuel = FULL_TANK

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

        return self.fuel

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if not self.engine_on:
            return 'Engine is off.  Cannot drive.'
        if miles_to_drive <= 0:
            return 'Miles to drive must be positive.'

        max_possible_dis = self.fuel * self.mpg
        if miles_to_drive > max_possible_dis:
            miles_to_drive = max_possible_dis
            self.fuel = 0.0
        else:
            self.fuel -= miles_to_drive / self.mpg

        self.odometer += miles_to_drive
        if self.fuel == 0.0:
            self.engine_on = False

        # Type your code here and remove the return statement

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        if self.engine_on:
            return 'Cannot add gas while engine is on.'
        if amount_to_add <= 0:
            return 'Amount must be positive.'
        self.fuel = min(self.fuel + amount_to_add, FULL_TANK)

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement

        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement

        self.engine_on = False