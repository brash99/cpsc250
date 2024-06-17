FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", mpg=24.0):
        # Type your code here.
        self.make = make
        self.mpg = mpg
        #return make, mpg  #I'm trying to call both make and mpg back so i can reference them in the main
    # Return car model
    def get_model(self, model):
        self.model = model
        #model = str(input()) #This line is in the main
        return model #here im calling the model

    # Return car odometer
    def check_odometer(self, odom= 5):
        # Update the return statment.
        self.odom = odom
        return odom #im returning the odom param and its default value

    # Return miles per gallon (MPG)
    def get_mpg(self,mpg):
        self.mpg = mpg
        return mpg #im returning the mpg

    # Return amount of gas in tank
    def check_gas_gauge(self, gas_g=FULL_TANK):
        # Update the return statment.
        self.gas_g = gas_g
        return gas_g #with the default being FULL_TANK, returning gas_g

    # Honk horn
    def honk_horn(self, honk):
        self.honk = honk
        return print(f'The {self.model} says beep beep!') #returns print statement

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        self.miles_to_drive = miles_to_drive #initializing miles_to_dirve
        if self.gas_g > 0: #if gas in the tank
            self.odom = self.miles_to_drive/self.mpg #show how many miles i can drive on the current amount of gas in tank
            return start_engine #start the engine
        elif self.gas_g == 0: # if no gas in the tank
            self.odom = 0 #odom = 0
            return stop_engine #engine won't turn on or will stop once no gas(gas_g = 0)
        # Add gas to tank. Check for positive value of amount to add

    def add_gas(self, amount):
        self.amount = amount
        if self.amount > 0: #as long as amount isnt 0
            if gas_g < FULL_TANK:# and if theres less than the full amount in the tank
                gas_g = gas_g + amount #add the amount of however much is already in the tank to current gas in tank


        # Set boolean variable to True

    def start_engine(self, start):
        # Type your code here and remove the return statement
        self.start = True #start_engine = true

        # Set boolean variable to False
    def stop_engine(self, stop):
        # Type your code here and remove the return statement
        self.stop = False #stop_engine = false

#I am not sure how to properly test the code. I attempted to give fancy car parameters but im not sure
#how to go about testing the FancyCar program
if __name__ == '__main__':
    model = str(input())
    fancy_car = model,mpg
    my_car = fancy_car.FancyCar()


    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")