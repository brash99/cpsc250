import fancy_car_Joseph_Simon

if __name__ == '__main__':
    my_car = fancy_car_Joseph_Simon.FancyCar()

    # Testing initial values
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")

    # Testing driving and checking odometer and gas gauge
    my_car.start_engine()
    my_car.drive(50)
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")

    # Testing adding gas and checking gas gauge
    my_car.add_gas(5)
    print(f"gas_tank={my_car.check_gas_gauge()}")

    # Testing honking horn
    my_car.honk_horn()

    # Testing stopping engine
    my_car.stop_engine()

    # Testing trying to drive without starting the engine
    my_car.drive(10)
