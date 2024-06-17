# UNCOMPLETED class definition FancyCar
FULL_TANK = 14.0

class FancyCar:
    def __init__(self, model="Old Clunker", mpg=24.0):
        self.model = model
        self.mpg = mpg
        self.odometer = 5
        self.engine_on = False
        self.fuel = FULL_TANK

    # Step
    def check_odometer(self):
        return
    def check_gas_gauge(self):
        return

    def get_model(self):
        return

    def get_mpg(self):
        return

    # Step 2: Instance method to honk horn
    def honk_horn(self):
        return

    # Step 3: Instance method to drive
    def drive(self, miles_to_drive):
        return

    # Step 4: Instance method to add gas
    def add_gas(self, amount):
        return

    # Step 6: Instance methods to start and stop the engine
    def start_engine(self):
        return

    def stop_engine(self):
        return

# Test the FancyCar class with incomplete methods
def main():
    car = FancyCar("Honda Civic", 30.0)
    car.start_engine()
    print(f"Odometer: {car.check_odometer()} miles")
    print(f"Gas gauge: {car.check_gas_gauge()} gallons")
    car.honk_horn()
    car.drive(100)
    print(f"Odometer after driving 100 miles: {car.check_odometer()} miles")
    print(f"Gas gauge after driving 100 miles: {car.check_gas_gauge()} gallons")
    car.add_gas(5)
    print(f"Gas gauge after adding 5 gallons: {car.check_gas_gauge()} gallons")
    car.stop_engine()
    car.add_gas(5)
    print(f"Gas gauge after adding another 5 gallons with engine off: {car.check_gas_gauge()} gallons")

if __name__ == "__main__":
    main()