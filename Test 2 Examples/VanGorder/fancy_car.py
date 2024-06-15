FULL_TANK = 14
class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.gas_in_tank = FULL_TANK
        self.engine_started = False

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
        return self.gas_in_tank

    # Honk horn
    def honk_horn(self):
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if miles_to_drive <= 0:
            print('Miles to drive must be positive.')
            return
        if not self.engine_started:
            print('Cannot drive Engine is not started.')

    # Add gas to tank. Check for positive value of amount to add
        max_distance = self.gas_in_tank * self.mpg
        if miles_to_drive > max_distance:
            miles_to_drive = max_distance

        self.odometer += miles_to_drive
        gas_used = miles_to_drive/self.mpg
        self.gas_in_tank -= gas_used

        if self.gas_in_tank <= 0:
            self.gas_in_tank = 0.0
            self.engine_started = False
            print("Out of gas! Engine stopped.")
        else:
            print(f'Driving {miles_to_drive} miles.')
    def add_gas(self, amount_to_add):
        if amount_to_add <= 0:
            print("Amount to add must be positive.")
            return
        if self.engine_started:
            print('Cannot add gas. Engine is still running.')

        self.gas_in_tank += amount_to_add
        if self.gas_in_tank > FULL_TANK:
            self.gas_in_tank = FULL_TANK
        print(f'Added {amount_to_add} gallons of gas.')

    # Set boolean variable to True
    def start_engine(self):
        if self.engine_started:
            print("Engine is already started.")
        else:
            self.engine_started = True
            print("Engine started.")

     # Set boolean variable to False
    def stop_engine(self):
        if not self.engine_started:
            print("Engine is already stopped.")
            return
        else:
            self.engine_started = False
            print("Engine is stopped.")
