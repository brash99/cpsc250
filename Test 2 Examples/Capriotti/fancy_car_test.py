import fancy_car

if __name__ == '__main__':
    #my_car = fancy_car.FancyCar()
    my_car = fancy_car.FancyCar("Toyota Corolla", 15.5, 1000, True, 2)

    # Just for initial testing
    #print("Default values:")
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")
    print("Is the engine on? ", end="")
    if my_car.engine_on:
        print("Yes")
        print("Stopping engine...")
        my_car.stop_engine()
        print("Is the engine off now? ", end="")
        if my_car.engine_on:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
        print("Starting engine...")
        my_car.start_engine()
        print("Is the engine on now? ", end="")
        if my_car.engine_on:
            print("Yes")
        else:
            print("No")

    my_car.stop_engine()
    print("Drive 100 miles")
    my_car.drive(100)
    print("Start the engine")
    my_car.start_engine()
    print("Okay, NOW drive 100 miles")
    my_car.drive(100)
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")
    print("How about 0 miles?")
    my_car.drive(0)
    print("And negative miles?")
    my_car.drive(-100)

    print("Add 1000 gallons of gas")
    my_car.add_gas(1000)
    my_car.stop_engine()
    print("Okay, NOW add 1000 gallons of gas")
    my_car.add_gas(1000)
    print(f"gas_tank={my_car.check_gas_gauge()}")
    print("How about 0 gallons?")
    my_car.add_gas(0)
    print("And negative gallons?")
    my_car.add_gas(-1000)
    my_car.honk_horn()
