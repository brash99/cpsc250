class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def groom_pet(self):
        pass

    def pet_pet(self):
        pass

class Dog(Pet):

    def __init__(self, name, age, number_of_legs, danger_level):
        Pet.__init__(self,name, age)
        self.number_of_legs = number_of_legs
        self.danger_level = danger_level

    def set_number_of_legs(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def set_danger_level(self, danger_level):
        self.danger_level = danger_level

    def get_number_of_legs(self):
        return self.number_of_legs

    def get_danger_level(self):
        return self.danger_level

    def groom_pet(self):
        print(f"Brushing my dog's hair!")

    def pet_pet(self):
        print(f"Who’s a good boooooooy?")

    def __str__(self):
        return f"My dog {self.name} is adorable, they are {self.age} years old!!"

    def __eq__(self, other):
        return (self.name == other.name and self.age == other.age and
                self.number_of_legs == other.number_of_legs and
                self.danger_level == other.danger_level)

class Alligator(Pet):

    def __init__(self, name, age, tail_length, number_of_teeth, danger_level):
        Pet.__init__(self, name, age)
        self.tail_length = tail_length
        self.number_of_teeth = number_of_teeth
        self.danger_level = danger_level

    def set_tail_length(self, tail_length):
        self.tail_length = tail_length

    def set_number_of_teeth(self, number_of_teeth):
        self.number_of_teeth = number_of_teeth

    def set_danger_level(self, danger_level):
        self.danger_level = danger_level

    def get_tail_length(self):
        return self.tail_length

    def get_number_of_teeth(self):
        return self.number_of_teeth

    def get_danger_level(self):
        return self.danger_level

    def groom_pet(self):
        print(f"Yeah … no … you look good.")

    def pet_pet(self):
        print(f"Imma just be over here 100 feet away.")

    def __str__(self):
        return f"My alligator {self.name} is definitely an alligator and is not a crocodile.  You can tell because they have {self.number_of_teeth} teeth and their tail is {self.tail_length} feet long."

    def __eq__(self, other):
        return True


if __name__ == '__main__':
    Bailey = Dog("Bailey", 7, 4, "Angry")
    print(Bailey)  # My dog Bailey is adorable, they are 7 years old!!
    KillingMachine = Alligator("Tiny", 47, 15,
                               100, "Killer")
    print(KillingMachine)  # My alligator Tiny is definitely an alligator and is not a crocodile.
                            # You can tell because they have 100 teeth and their
                            # tail is 15 feet long.
    print()

    Juniper = Dog("Junyper", 0, 2, "Happy")
    Juniper.set_number_of_legs(4)
    Juniper.set_danger_level("Happiest")
    Juniper.set_name("Juniper")
    Juniper.set_age(1)
    print(Juniper)  # My dog Juniper is adorable, they are 1 years old!!
    print(Juniper.get_number_of_legs())  # 4
    print(Juniper.get_danger_level())  # Happiest

    print(Bailey == Juniper) # False
    print(KillingMachine == Alligator("Generic", 43, 45,
                                      100,"Whatever"))  # True

    Bailey.groom_pet() # Brushing my dog's hair!
    print()
    Bailey.pet_pet() # Who’s a good boooooooy?
    print()
    KillingMachine.groom_pet() # Yeah … no … you look good.
    print()
    KillingMachine.pet_pet() # Imma just be over here 100 feet away.
    print()