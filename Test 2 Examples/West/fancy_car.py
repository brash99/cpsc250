FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.mpg = mpg
        self.odometer = 5
        self.engine_status = False
        self.gas_tank = FULL_TANK
        self.model = make

    # Return car model
    def get_model(self):
        # Update the return statment.

        return self.model

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
        print(f'The {self.model} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if self.gas_tank == 0:
            self.gas_tank = 0
        elif miles_to_drive > 0:
            self.odometer += miles_to_drive
            self.gas_tank -= miles_to_drive / self.mpg

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):

        if self.engine_status == True and amount_to_add > 0:
            self.gas_tank += amount_to_add
            if self.gas_tank > FULL_TANK:
                self.gas_tank = FULL_TANK

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement

        self.engine_status = True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement

        self.engine_status = False
