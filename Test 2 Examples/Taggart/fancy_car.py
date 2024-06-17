FULL_TANK = 14
class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.make = make
        self.odometer = 5
        self.mpg = mpg
        self.gas_gauge = FULL_TANK
        self.engine_on = False


    def get_model(self):
        return self.make

    def check_odometer(self):
        return self.odometer

    def get_mpg(self):
        return self.mpg

    def check_gas_gauge(self):
        return self.gas_gauge

    def honk_horn(self):
        print('The {self.make} says beep beep!')

    def drive(self, miles_to_drive):
        max_distance = self.gas_gauge * self.mpg
        if max_distance < miles_to_drive:
            self.odometer += miles_to_drive - max_distance
            self.gas_gauge = 0.0
        elif self.engine_on and miles_to_drive > 0:
            self.odometer += miles_to_drive
            self.gas_gauge -= (miles_to_drive / self.mpg)

    def add_gas(self, amount_to_add):
        if amount_to_add > 0 and self.engine_on == True:
            self.gas_gauge = min(self.gas_gauge + amount_to_add, FULL_TANK)
        # Type your code here and remove the return statement
        # Set boolean variable to True
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
