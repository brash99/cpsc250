FULL_TANK = 14

class FancyCar:
    #def __init__(self, make="Old Clunker", mpg=24.0, model ="", odometer = 0, gas_gauge=0, honk_horn= '' ):
    def __init__(self, make="Old Clunker", mpg=24.0, model ="", odometer = 0, gas_gauge=0):
        self.mpg = mpg
        self.make = make
        self.model = model
        self.odometer = odometer
        self.gas_gauge = gas_gauge
        #self.honk_horn = honk_horn
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

        return 0.0

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.

        return 0.0

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print('beeeeeeeep')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if miles_to_drive > 0:

            return self.miles_to_drive

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if amount_to_add > 1:

            return self.amount_to_add

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        self.start_engine = True
        return self.start_engine

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        self.stop_engine = False
        return self.stop_engine
