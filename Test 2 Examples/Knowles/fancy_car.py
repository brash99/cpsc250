FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        self.make = make
        self.mpg = mpg #miles per gallon function on the ol' clunker here
        self.odometer = 5 #set the odometer to the 5 miles specified
        self.engine_on = False #set the boolean on and off variable to false
        self.fuel = FULL_TANK #funtion to set the fuel in the car to a full tank

    # Return car model
    def get_model(self):
        # Update the return statment.

        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.

        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.

        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.

        return self.fuel

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print(f"The {self.make} says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if self.engine_on and miles_to_drive > 0:  #checking to make sure that the car is in fact on and has gas in it
            max_distance = self.fuel * self.mpg
            if miles_to_drive <= max_distance:
                    self.odometer += miles_to_drive
                    self.fuel -= miles_to_drive / self.mpg
            else:
                    self.odometer += max_distance
                    self.fuel = 0.0
                    self.engine_on = False #engine would turn off if the car ran out of gas!!
        elif not self.engine_on:
            print("The engine is off! Start the engine first.")


        return -1

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if not self.engine_on and amount_to_add > 0:
            self.fuel = min(self.fuel + amount_to_add, FULL_TANK) #the min amount needed to fuel the car



    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True



    # Set boolean variable to False
    def stop_engine(self):
        self.engine_on = False

#run the "__main__" to test and put the actual code