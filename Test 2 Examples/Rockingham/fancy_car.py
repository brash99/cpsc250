FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.engine_status = False
        self.fuel_status = FULL_TANK

    # Return car model
    def get_model(self):
        return self.make

    def check_odometer(self):
        return self.odometer

    def get_mpg(self):
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        return self.fuel_status

    # Honk horn
    def honk_horn(self):
        print(f"The {self.make} says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if self.engine_status and miles_to_drive > 0:
            dist = self.fuel_status * self.mpg
            if miles_to_drive > dist:
                print(f"The car can only drive up to {dist} miles due fuel amount.")
                miles_to_drive = dist
            self.odometer += miles_to_drive
            self.fuel_status -= miles_to_drive / self.mpg

            if self.fuel_status <= 0:
                self.fuel_status = 0
                self.engine_status = False
                print("The car is out of gas and engine can't run")
        else:
            print("The car isn't on or the distance is non-positive")

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        if not self.engine_status and amount_to_add > 0:
            self.fuel_status += amount_to_add
            print(f"Added {amount_to_add} gallons of gas to the tank.")
        elif self.engine_status:
            print("Can't add gas while engine is on.")
        elif amount_to_add <= 0:
            print('Amount must be greater than 0.')

    # Set boolean variable to True
    def start_engine(self):
        self.engine_status = True
        print("The engine is ready!")

    # Set boolean variable to False
    def stop_engine(self):
        self.engine_status = False
        print("The engine is stopped!")

if __name__ == "__main__":
    #Chatgpt generated examples
    car = FancyCar("Honda Civic", 10.0)
    print(car.get_model())  # Honda Civic
    print(car.check_odometer())  # 5
    print(car.get_mpg())  # 30.0
    print(car.check_gas_gauge())  # 14

    car.honk_horn()  # The Honda Civic says beep beep!
    car.start_engine()
    car.drive(10)  # Drives the car 100 miles if possible
    print(car.check_odometer())  # Updated odometer
    print(car.check_gas_gauge())  # Updated fuel status

    car.stop_engine()
    car.add_gas(20)  # Adds gas if engine is off