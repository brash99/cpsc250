FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        #STEP 0
        self.make = make #initialize make
        self.mpg = mpg #initialize mpg
        self.odometer = 5 #initialize odometer
        self.engine = False #Engine on/off Boolean to False
        self.gas = FULL_TANK #fuel in gastank = full_tank

    # Return car model
    def get_model(self):
        # Update the return statment.
        #STEP 1

        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        #STEP 1

        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        #STEP 1

        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.
        #STEP 1

        return self.gas

    # Honk horn
    def honk_horn(self):
        #STEP 2
        # Type your code here.
        print(f'The {self.make} says beep beep!') #output to identify car model

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        #STEP 3
        if miles_to_drive > 0 and self.engine: #checking if its positive
            maximum_miles_to_drive = self.gas * self.mpg #calculation of checking how much miles the car can drive
            if miles_to_drive > maximum_miles_to_drive:
                miles_to_drive = maximum_miles_to_drive
                self.gas = 0.0 #setting gas level to 0
                self.engine = False
            else:
                self.gas -= miles_to_drive / self.mpg #the amount of gas in the tank should decrease
                self.odometer += miles_to_drive #odometer increase by miles_to_drive


    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        #STEP 4
        if amount_to_add > 0 and not self.engine: #
            self.gas = min(self.gas + amount_to_add, FULL_TANK) #updating to only add gas if the engine is off




    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        #STEP 6

        self.engine = True #setting to True

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        #STEP 6

        self.engine = False #setting to False
if __name__ == "__main__":
    my_car = FancyCar("Old Chunker", 24.0)
    print(my_car.get_model())
    print(my_car.get_mpg())
    print(my_car.check_odometer())
    print(my_car.check_gas_gauge())

    my_car.honk_horn()
    my_car.start_engine()
    my_car.drive(60)
    print(my_car.check_odometer())
    print(my_car.check_gas_gauge())

    my_car.add_gas(3.0)
    print(my_car.check_gas_gauge())

    my_car.stop_engine()
    my_car.add_gas(3.0)
    print(my_car.check_gas_gauge())