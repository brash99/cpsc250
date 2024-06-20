class TransportMode:
    def __init__(self, name, speed=75):
        self.name = name
        self.speed = speed

    def info(self):
        print(f'{self.name} can go {self.speed} mph.')


class MotorVehicle(TransportMode):
    def __init__(self, name, speed=80, mpg=40):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, dist):
        required_fuel = dist / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print(f'{self.fuel_gal:f} gallons remaining.')


class MotorCycle(MotorVehicle):
    def __init__(self, name, speed=55, mpg=25):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print(f'On a {self.name}, that is too dangerous.')


# Define two motorcycles, specifying all values
scooter = MotorCycle('Vespa', 55, 40)
dirtbike = MotorCycle('KX450F', 80, 25)

# Define some vehicles, specifying only the name ... note which
# default values are used :)
harley = MotorCycle('Harley Davidson')

# What are the default values for the harley object?
#
# name "Harley Davidson"
# speed 55
# mpg 25
# fuel_gal 0 (from MotorVehicle)

generic = MotorVehicle('PeopleCarrier')

# What are the default values for the generic object?
#
# name "PeopleCarrier"
# speed 80
# mpg 40
# fuel_gal 0


generic2 = TransportMode('MovingThing')

# What are the default values for the generic2 object?
#
# name "MovingThing"
# speed 75


scooter.info()
dirtbike.info()
harley.info()
generic.info()
generic2.info()


choice = input('Select scooter (s) or dirtbike (d): ')
if (choice == 's'):
    bike = scooter
else:
    bike = dirtbike

menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
command = input(menu)
while command != 'q':
    if command == 'f':
        fuel = int(input('Enter amount: '))
        bike.add_fuel(fuel)
    elif command == 'g':
        distance = int(input('Enter distance: '))
        bike.drive(distance)
    elif command == 'w':
        bike.wheelie()
    elif command == 'q':
        break
    else:
        print('Invalid command.')

    command = input(menu)
