FULL_TANK = 14

#Step 1.Complete the first four instance methods to check the odometer, check the gas gauge, get the model, and get the miles per gallon.
class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.gas = FULL_TANK

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
        return self.gas

    # Honk the horn
    def honk_horn(self):
        print(f"The {self.make} says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if miles_to_drive < 0:
            print("Must drive with positive amount of miles")
            return
        #not sure if I can add other print statements in program, but I added them anyway.
#update drive to determine if the car runs out of gas
        #find maximum distance
        max_distance = self.gas * self.mpg
        if miles_to_drive > max_distance:
            print(f"Ran out of gas.")
            self.odometer += max_distance
            self.gas = 0
            self.engine_on = False
        else:
            self.odometer += miles_to_drive
            self.gas -= miles_to_drive / self.mpg


    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if amount_to_add < 0:
            print("Cannot add negative amount of gas")
            return

        self.gas = (self.gas + amount_to_add, FULL_TANK)

    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True

    # Sett boolean variable to False
    def stop_engine(self):
        self.engine_on = False
