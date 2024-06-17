class FancyCar:
    FULL_TANK = 14  # Global variable for full tank capacity

    def __init__(self, make="Old Clunker", mpg=24.0):
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.fuel_in_tank = self.FULL_TANK

    def get_model(self):
        return self.make

    def check_odometer(self):
        return self.odometer

    def get_mpg(self):
        return self.mpg

    def check_gas_gauge(self):
        return self.fuel_in_tank

    def honk_horn(self):
        print(f"The {self.make} says beep beep!")

    # Assisted with Github Copilot and ChatGPT
    def drive(self, miles_to_drive):
        # Check if the engine is on and miles_to_drive is positive
        if self.engine_on and miles_to_drive > 0:
            max_distance = self.fuel_in_tank * self.mpg
            max_distance = self.fuel_in_tank * self.mpg
            if miles_to_drive <= max_distance:
                self.odometer += miles_to_drive
                self.fuel_in_tank -= miles_to_drive / self.mpg
            else:
                self.odometer += max_distance
                self.fuel_in_tank = 0.0
                self.engine_on = False
#Assisted with Github Copilot and ChatGPT
    def add_gas(self, amount_to_add):
        if not self.engine_on and amount_to_add > 0:
            self.fuel_in_tank += amount_to_add
            if self.fuel_in_tank > self.FULL_TANK:
                self.fuel_in_tank = self.FULL_TANK

    # Set the engine state to on (True)
    def start_engine(self):
        self.engine_on = True

    # Set the engine state to on (False)
    def stop_engine(self):
        self.engine_on = False


