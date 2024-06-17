FULL_TANK = 14


class FancyCar:
    def __init__(self, model="Old Clunker", mpg=24.0, odometer=5, engine=False):
        # Type your code here.
        self.model = model
        self.mpg = mpg
        self.odometer = odometer
        self.engine = engine
        self.tank = FULL_TANK

    # Return car model
    def get_model(self):
        # Update the return statment DONE

        return self.model

    # Return car odometer
    def check_odometer(self):
        # Update the return statment. DONE

        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.DONE

        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment. DONE

        return self.tank

    # Honk horn
    def honk_horn(self):
        # Type your code here.DONE
        print(f'The {self.get_model} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        if self.start_engine:
            if miles_to_drive > 0:
                if miles_to_drive <= self.mpg * self.tank:
                    self.odometer += miles_to_drive
                    self.tank -= miles_to_drive / self.mpg

                if miles_to_drive > self.mpg * self.tank:
                    self.odometer += self.mpg * self.tank
                    self.tank == 0.0

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        if not self.stop_engine():
            if amount_to_add > 0:
                if amount_to_add + self.tank <= FULL_TANK:
                    self.tank += amount_to_add

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        if self.tank > 0:
            return True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        if self.tank == 0:
            return False


