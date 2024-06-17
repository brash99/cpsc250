FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.model = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.fuel_remaining = FULL_TANK

    # Return car model
    def get_model(self):
        return self.model

    # Return car odometer
    def check_odometer(self):
        return round(self.odometer, 2)

    # Return miles per gallon (MPG)
    def get_mpg(self):
        return round(self.mpg, 2)

    # Return amount of gas in tank
    def check_gas_gauge(self):
        return round(self.fuel_remaining, 2)

    # Honk horn
    def honk_horn(self):
        print(f"The {self.model} says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if miles_to_drive > 0:
            if self.engine_on:
                max_distance = min(self.fuel_remaining * self.mpg, miles_to_drive)
                self.odometer += max_distance
                self.fuel_remaining -= max_distance / self.mpg
                if max_distance < miles_to_drive:
                    print("Out of gas!")
                    self.stop_engine()
            else:
                print("Might wanna turn the engine on. Or push.")
        else:
            print("How ya gonna drive negative miles silly?")

    # Set boolean variable to True
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
        else:
            print("Engine is already running no turbo charging.")

    # Set boolean variable to False
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
        else:
            print("How are ya gonna turn off an engine that's already off?")

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if amount_to_add > 0:
            if not self.engine_on:
                self.fuel_remaining = min(self.fuel_remaining + amount_to_add, FULL_TANK)
            else:
                print("Gotta stop the engine before adding gas. Or you'll explode")
        else:
            print("No siphoning gas input a positive number.")

