class DrivingMixin:
    def drive(self, distance):
        print(f'Driving {distance} miles ...')

    def change_tire(self):
        print('Changing a tire ...')

    def check_oil(self):
        print('Checking the oil ...')


class FlyingMixin:
    def fly(self, distance, altitude):
        print(f'Flying {distance} miles at {altitude} feet ...')

    def roll(self):
        print('Executing a roll ...')

    def eject(self):
        print('Ejecting!!! Yikes!!!')


class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f'{self.name} can go {self.speed} mpg')


class SemiTruck(TransportMode, DrivingMixin):
    def __init__(self, name, speed, cargo):
        TransportMode.__init__(self, name, speed)
        self.cargo = cargo

    def go(self, distance):
        self.drive(distance)
        # ...


class FlyingCar(TransportMode, FlyingMixin, DrivingMixin):
    def __init__(self, name, speed, max_altitude):
        TransportMode.__init__(self, name, speed)
        self.max_altitude = max_altitude

    def go(self, distance):
        self.fly(distance / 2, self.max_altitude)
        # ...
        self.drive(distance / 2)

if __name__ == '__main__':
    s = SemiTruck('MacTruck', 85, 'Frozen beans')
    f = FlyingCar('Jetson35K', 325, 15000)

    s.go(100)
    f.go(100)
