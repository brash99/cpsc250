FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.mpg = 24.0
        self.make = make

    # Return car model
    def get_model(self):
        # Update the return statment.

        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.

        return 5

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.

        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.

        return FULL_TANK

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f'{self.make} {self.model} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        if miles_to_drive > 0 and miles_to_drive <= 60:
            self.check_odometer() + miles_to_drive
            self.check_gas_gauge = self.FULL_TANK - miles_to_drive/self.mpg
        else:
            check_gas_gauge = 0



    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        while self.check_gas_gauge() < FULL_TANK:
            self.check_gas_gauge + self.amount_to_add



    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement

        return True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement

        return False

if __name__ == '__main__':
    '''import fancy_car'''
    my_car = FancyCar()

    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")