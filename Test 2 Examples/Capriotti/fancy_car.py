"""Creates a class named FancyCar with attributes make, mpg, odometer, engine_on, and gas_in_tank,
and functions get_model, check_odometer, get_mpg, check_gas_gauge, honk_horn, drive, add_gas,
start_engine, and stop_engine"""
'''I asked ChatGPT what was wrong with my program again. THIS time it only pointed out
a potential divide by 0 in the drive function (if mpg == 0), so I fixed that.
It also said my error messages were ""unprofessional"" but I thought my intended audience
would appreciate them.'''

FULL_TANK = 14
class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0, odometer=5, engine_on=False, gas_in_tank=FULL_TANK):
        # Type your code here.
        self.make = make
        self.mpg = mpg
        self.odometer = odometer
        self.engine_on = engine_on
        self.gas_in_tank = gas_in_tank

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
        if not self.engine_on:
            print("The engine must be on in order to drive.")
            return
        if self.mpg == 0:
            print("MPG is set to 0. Calling this function would \n"
                  "result in a divide by 0 error.\n"
                  "Change MPG to something else - a positive value \n"
                  "would be nice, but I'm not picky.")
            return
        if miles_to_drive > 0:
            if miles_to_drive <= self.gas_in_tank * self.mpg:
                self.odometer += miles_to_drive
                self.gas_in_tank -= miles_to_drive / self.mpg
            else:
                self.odometer += self.gas_in_tank * self.mpg
                self.gas_in_tank = 0.0
        elif miles_to_drive == 0:
            print("You entered 0 miles.\n"
                  "After a long and grueling drive, \n"
                  "you realize... You forgot the car.\n"
                  "Maybe try entering a positive number instead.")
        else:
            print("You entered a negative number of miles.\n"
                  "Look, time travel is outside of the scope of this program.\n"
                  "Maybe try entering a positive number instead.")

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if self.engine_on:
            print("The engine must be off in order to add gas.")
        if amount_to_add > 0:
            self.gas_in_tank += amount_to_add
            if self.gas_in_tank > FULL_TANK:
                self.gas_in_tank = FULL_TANK
        elif amount_to_add == 0:
            print("You entered 0 gallons.\n"
                  "You drive up to the gas station and realize... \n"
                  "You forgot your wallet.\n"
                  "You decide to drive under the speed limit on the way home.\n"
                  "Maybe try adding a positive number instead.")
        else:
            print("You entered a negative number of gallons.\n"
                  "Listen, siphoning is outside of the scope of this program.\n"
                  "Maybe try adding a positive number instead.")

    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        self.engine_on = False
