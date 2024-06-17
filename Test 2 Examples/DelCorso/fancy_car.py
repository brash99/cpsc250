FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        # the name of the car
        self.make = make
        # the miles per gallons
        self.mpg = mpg
        #the odometer
        self.odometer = 5
        #is the car on or off?
        self.engine_on = False
        # the fuel
        self.fuel_in_tank = FULL_TANK

    # Return car model
    def get_model(self):
        # Update the return statment.
        #gets the car model
        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        #checks the cars odometer
        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.
        #checking the fuel.
        return self.fuel_in_tank

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        # ex: the Ford Mustang says beep beep!
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        # if the engine is false and miles_to_drive is bigger and not 0.
        if self.engine_on and miles_to_drive > 0:
            max_distance = self.fuel_in_tank * self.mpg
            if miles_to_drive > max_distance:
                #adds to odometer
                self.odometer += max_distance
                #out of gasssss
                self.fuel_in_tank = 0.0
                self.engine_on = False
            else:
                self.odometer += miles_to_drive
                self.fuel_in_tank -= miles_to_drive/self.mpg
            return 0
        else:
            return -1

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        # adds to the fuel/ gas to the car.
        if not self.engine_on and amount_to_add >0:
            self.fuel_in_tank= min(self.fuel_in_tank +amount_to_add, FULL_TANK)
            return 0
        else:
            return -1

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        if not self.engine_on and self.fuel_in_tank >0:
            self.engine_on = True
            #is the engine up and running?
            return 0
        else:
            return -1

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        if self.engine_on:
            self.engine_on = False
            #stop engines.
            return 0
        else:
            return -1