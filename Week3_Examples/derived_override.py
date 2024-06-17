class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def get_name(self):
        return self.name

    def set_quantity(self, qnty):
        self.quantity = qnty

    def get_quantity(self):
        return self.quantity

    def display(self):
        print(self.name, self.quantity)


class Produce(Item):  # Derived from Item
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.expiration = ''

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration

    def display(self):
        print(self.name, self.quantity)
        print(f'  Expires: {self.get_expiration()}')


class Banana(Produce):  # Derived from Produce
    def __init__(self):
        Produce.__init__(self)
        self.color = ''

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def display(self):
        print(self.name, self.quantity)
        print(f'  Expires: {self.get_expiration()}')
        print(f'  Color: {self.get_color()}')


item1 = Item()
item1.set_name('Cereal')
item1.set_quantity(9)
item1.display()

item2 = Produce()
item2.set_name('Apples')
item2.set_quantity(20)
item2.set_expiration('8/5/2024')
item2.display()


item3 = Banana()
item3.set_name('Chiquita')
item3.set_quantity(50)
item3.set_expiration('7/4/2024')
item3.set_color('yellow')
item3.display()
