class Winged:
    def __init__(self, wingspan):
        self.wingspan = wingspan

    def flap_wings(self):
        print('Flapping my wings ...')

    def blink(self):
        print('Winged: blinking ...')


class Mammal:
    def breathe(self):
        print('Breathing ...')

    def give_birth(self):
        print('Giving birth now ... ouch!')
    def blink(self):
        print('Mammal: blinking ...')


class Bat(Mammal, Winged):

    def __init__(self, wingspan):
        Winged.__init__(self, wingspan)


if __name__== '__main__':

    dracula = Bat(10.30)

    dracula.breathe()
    dracula.breathe()
    dracula.give_birth()
    dracula.flap_wings()
    dracula.breathe()
    dracula.blink() # Which blink method is called? Winged or Mammal?
