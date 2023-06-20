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


class Banana(Produce):  # Derived from Produce
    def __init__(self):
        Produce.__init__(self)
        self.color = ''

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


item1 = Item()
item1.set_name('Cereal')
item1.set_quantity(9)
item1.display()

item2 = Produce()
item2.set_name('Apples')
item2.set_quantity(20)
item2.set_expiration('8/5/2023')
item2.display()
print(f'  Expires: {item2.get_expiration()}')

item3 = Banana()
item3.set_name('Chiquita')  # Item class
item3.set_quantity(50)  # Item class
item3.set_expiration('7/4/2023')  # Produce class
item3.set_color('yellow')  # Banana class
item3.display()  # Item class
print(f'  Expires: {item3.get_expiration()}')  # Produce class
print(f'  Color: {item3.get_color()}')  # Banana class

