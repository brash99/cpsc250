FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # init the car model with the given make or default to Old Clunker
        self.make = make
        # init the car's fuel efficiency (miles per gallon) with the given value or default to 24.0
        self.mpg = mpg
        # init the odometer to start at 5 miles
        self.odometer = 5
        # init the engine state to be off (False)
        self.engine_on = False
        # init the amount of fuel in the gas tank to a full tank
        self.fuel_in_tank = FULL_TANK

    # Return car model
    def get_model(self):
        return self.make

    # Return the current car odometer reading
    def check_odometer(self):
        return self.odometer

    # Return the mpg of the car
    def get_mpg(self):
        return self.mpg


    # Return amount of gas they have in the tank currently
    def check_gas_gauge(self):
        return self.fuel_in_tank

    # print the cars make along with it beeping its horn
    def honk_horn(self):
        print(f'The {self.make} says beep beep!')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Check if the engine is on before driving
        if not self.engine_on:
            print("Engine is off. Start the engine first.")
            return
            # Calculate the maximum distance the car can drive with the current fuel
            if miles_to_drive > 0:
                return
            # Only proceed if the requested miles to drive is positive
            # received this part of the code from chat gpt,
            # I found it difficult to understand so I looked it up and have a better understanding now
            max_possible_distance = self.fuel_in_tank * self.mpg

            # Adjust the miles to drive if it exceeds the maximum possible distance
            if miles_to_drive > max_possible_distance:
                miles_to_drive = max_possible_distance

            # Update the odometer reading with the actual miles driven
            self.odometer += miles_to_drive
            # Decrease the fuel in the tank based on the miles driven
            self.fuel_in_tank -= miles_to_drive / self.mpg

            # If the car runs out of gas, stop the engine
            if self.fuel_in_tank <= 0:
                self.fuel_in_tank = 0.0
                self.stop_engine()

    # Add gas to the tank and make sure the car is off
    def add_gas(self, amount_to_add):
        # Check if the engine is off before refueling
        if self.engine_on:
            print("Turn off the engine before refueling.")
            return
        # Only proceed if the amount of gas to add is positive
        if amount_to_add > 0:
            # Add gas to the tank without overfilling the tank
            self.fuel_in_tank = min(FULL_TANK, self.fuel_in_tank + amount_to_add)

    # Set boolean variable to True
    # start the engine
    def start_engine(self):
        self.engine_on = True

    # Set boolean variable to False
    # turn the engine off
    def stop_engine(self):
        self.engine_on = False