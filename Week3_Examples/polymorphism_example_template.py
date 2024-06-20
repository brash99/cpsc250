class Pet:
    pass

class Dog(Pet):
    pass

class Alligator(Pet):
    pass

if __name__ == '__main__':
    Bailey = Dog("Bailey", 7, 4, "Angry")
    print(Bailey)  # My dog Bailey is adorable, they are 7 years old!!
    KillingMachine = Alligator("Tiny", 47, 15, 100, "Killer")
    print(KillingMachine)  # My alligator Tiny is definitely an alligator and is not a crocodile.  You can tell because they have 100 teeth and their tail is 15 feet long.
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
    print(KillingMachine == Alligator("Generic", 43, 45, 100,"Whatever"))  # True

    Bailey.groom_pet()
    print()
    Bailey.pet_pet()
    print()
    KillingMachine.groom_pet()
    print()
    KillingMachine.pet_pet()
    print()