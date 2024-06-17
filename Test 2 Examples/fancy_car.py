FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24):
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_on =  False
        self.gas_tank = FULL_TANK

    # Return car model
    def get_model(self):
        return self.make

    # Return car odometer
    def check_odometer(self):
        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        return self.gas_tank

    # Honk horn
    def honk_horn(self):
        print(f'The { self.make } says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Only drive if engine is on
        if miles_to_drive > 0 and self.engine_on:
            # calculate amount of gas needed for this trip
            gas_needed = miles_to_drive / self.mpg

            if gas_needed < self.gas_tank:
                # Car has enough gas
                self.odometer += miles_to_drive
                self.gas_tank -= gas_needed
            else:
                # Car runs out of gas
                distance = self.gas_tank * self.mpg
                self.odometer = self.odometer + distance
                self.gas_tank = 0
                self.engine_on = False

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Confirm engine is off
        if not self.engine_on:
            # what if negative number?
            if amount_to_add > 0:
                self.gas_tank += amount_to_add
                #What if too much?
            if self.gas_tank > FULL_TANK:
                self.gas_tank = FULL_TANK

    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        self.engine_on = False