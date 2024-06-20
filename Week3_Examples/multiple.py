class Winged:
    def __init__(self, wingspan):
        print('Winged: __init__ called ...')
        self.wingspan = wingspan

    def flap_wings(self):
        print('Flapping my wings ...')

    def blink(self):
        print('Winged: blinking ...')


class Mammal:

    def __init__(self):
        print('Mammal: __init__ called ...')

    def breathe(self):
        print('Breathing ...')

    def give_birth(self):
        print('Giving birth now ... ouch!')
    def blink(self):
        print('Mammal: blinking ...')


class Bat(Mammal, Winged):

    def __init__(self, wingspan):
        Mammal.__init__(self)
        Winged.__init__(self, wingspan)


if __name__== '__main__':

    dracula = Bat(10.30)

    dracula.breathe()
    dracula.breathe()
    dracula.give_birth()
    dracula.flap_wings()
    dracula.breathe()
    dracula.blink() # Which blink method is called? Winged or Mammal?
