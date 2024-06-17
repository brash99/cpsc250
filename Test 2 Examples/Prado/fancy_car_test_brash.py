from fancy_car import FancyCar

def test_passed1(test_feedback):

    car = FancyCar()

    if car.check_odometer() != 5:
        test_feedback.write(
            f"car should start with 5 miles but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < 13.9 or car.check_gas_gauge() > 14.1:
        test_feedback.write(f"car should start with 14.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    if car.get_mpg() < 23.9 or car.get_mpg() > 24.1:
        test_feedback.write(f"car should have MPG of 24.0 but get_mpg() returned {car.get_mpg()}")
        return False

    if car.get_model() != "Old Clunker":
        test_feedback.write(f"car model should be Old Clunker but get_model() returned {car.get_model()}")
        return False

    test_feedback.write("Constructor correctly initialized fields")

    return True

def test_passed2(test_feedback):

    car = FancyCar("65 Mustang", 29.5)

    if car.check_odometer() != 5:
        test_feedback.write(f"car should start with 5 miles but check_odometer() returned {car.check_odometer}")
        return False

    if car.check_gas_gauge() < 13.9 or car.check_gas_gauge() > 14.1:
        test_feedback.write(f"car should start with 14.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    if car.get_mpg() < 29.4 or car.get_mpg() > 29.6:
        test_feedback.write(f"car should have MPG of 29.5 but get_mpg() returned {car.get_mpg()}")
        return False

    if car.get_model() != "65 Mustang":
        test_feedback.write("car model should be 65 Mustang but get_model() returned car.get_model()}")
        return False

    test_feedback.write("Constructor correctly initialized the fields.")
    return True


import io
import sys
def test_passed3(test_feedback):
    car = FancyCar("65 Mustang", 29.5)

    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # redirect output

    car.honk_horn()

    sys.stdout = sys.__stdout__  # Reset redirect.

    expected_output = f"The {car.get_model()} says beep beep!\n"
    program_output = captured_output.getvalue()

    if program_output == expected_output:
        test_feedback.write(f"honk_horn() correctly outputted: {program_output}")
        return True
    else:
        test_feedback.write(f"honk_horn() incorrectly outputted: {program_output}")
        return False

def test_passed4(test_feedback):
    car = FancyCar("65 Mustang", 10.0)
    car.start_engine()
    car.drive(100)

    if car.check_odometer() != 105:
        test_feedback.write(f"odometer should be 105 miles after driving 100 but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < 3.9 or car.check_gas_gauge() > 4.1:
        test_feedback.write(f"car should have 4.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    car.drive(20)
    if car.check_odometer() != 125:
        test_feedback.write(f"odometer should be 125 miles after driving 120 but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < 1.9 or car.check_gas_gauge() > 2.1:
        test_feedback.write(f"car should have 2.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    # negative miles should be ignored
    car.drive(-100)
    if car.check_odometer() != 125:
        test_feedback.write("odometer should not change if attempting to drive negative miles")
        return False

    test_feedback.write("drive() correctly updated the odometer and gas tank for positive and negtive values.")
    return True

def test_passed5(test_feedback):
    car = FancyCar("65 Mustang", 10.0)
    car.start_engine()
    car.drive(100)
    car.stop_engine()
    car.add_gas(5)
    if car.check_gas_gauge() < 8.9 or car.check_gas_gauge() > 9.1:
        test_feedback.write(f"car should have 9.0 gallons of gas after adding 5.0 but check_gas_gauge() returned " + str(car.check_gas_gauge()))
        return False

    car.add_gas(-5)
    if car.check_gas_gauge() < 8.9 or car.check_gas_gauge() > 9.1:
        test_feedback.write("gallons of gas should not change after attempting to add -5.0")
        return False

    car.add_gas(50)
    if car.check_gas_gauge() < 13.9 or car.check_gas_gauge() > 14.1:
        test_feedback.write(f"amount of gas should not exceed 14.0 after attempting to add 50.0 but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    test_feedback.write("add_gas() correctly updated the gas tank for postive and negative values.")
    return True

def test_passed6(test_feedback):
    car = FancyCar("65 Mustang", 10.0)
    car.start_engine()
    car.drive(100)

    if car.check_odometer() != 105:
        test_feedback.write(f"odometer should be 105 miles after driving 100 but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < 3.9 or car.check_gas_gauge() > 4.1:
        test_feedback.write(f"car should have 4.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    car.drive(100)
    if car.check_odometer() != 145:
        test_feedback.write(f"odometer should be 145 after running out of gas but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < -0.01 or car.check_gas_gauge() > 0.01:
        test_feedback.write(f"car should have 0.0 gallons after running out of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    test_feedback.write(f"drive() correctly handled running out of gas.")
    return True

def test_passed7(test_feedback):
    car = FancyCar("65 Mustang", 10.0)
    car.drive(50)
    if car.check_odometer() != 5:
        test_feedback.write(f"car should not drive if engine is off but check_odometer() returned {car.check_odometer()}")
        return False

    car.start_engine()
    car.drive(50)

    if car.check_odometer() != 55:
        test_feedback.write(f"odometer should be 55 miles after driving 50 but check_odometer() returned {car.check_odometer()}")
        return False

    if car.check_gas_gauge() < 8.9 or car.check_gas_gauge() > 9.1:
        test_feedback.write(f"car should have 9.0 gallons of gas but check_gas_gauge() returned {car.check_gas_gauge()}")
        return False

    car.add_gas(5)
    if car.check_gas_gauge() < 8.9 or car.check_gas_gauge() > 9.1:
        test_feedback.write(f"should not be able to add gas if engine is running)")
        return False

    # should not be allowed to add gas if ngine off after running out of gas
    car.drive(200)
    car.add_gas(15)
    if car.check_gas_gauge() < 13.9 or car.check_gas_gauge() > 14.1:
        test_feedback.write(f"engine should have turned off after running out of gas")
        return False

    test_feedback.write("Passed:\n")
    test_feedback.write(f"  Car can not be driven unless the engine is on.\n")
    test_feedback.write(f"  Gas can not be added unless the engine is off.")
    return True

if __name__ == "__main__":

    total_points = 0

    test_feedback = io.StringIO()

    if test_passed1(test_feedback):
        test_feedback.write("\n")
        total_points += 1
    else:
        test_feedback.write("\n")

    if test_passed2(test_feedback):
        test_feedback.write("\n")
        total_points += 1
    else:
        test_feedback.write("\n")

    if test_passed3(test_feedback):
        test_feedback.write("\n")
        total_points += 1
    else:
        test_feedback.write("\n")

    if test_passed4(test_feedback):
        test_feedback.write("\n")
        total_points += 1
    else:
        test_feedback.write("\n")

    if test_passed5(test_feedback):
        test_feedback.write("\n")
        total_points += 2
    else:
        test_feedback.write("\n")

    if test_passed6(test_feedback):
        test_feedback.write("\n")
        total_points += 2
    else:
        test_feedback.write("\n")

    if test_passed7(test_feedback):
        test_feedback.write("\n")
        total_points += 2
    else:
        test_feedback.write("\n")

    print(test_feedback.getvalue())
    test_feedback = io.StringIO()

    print(f"Total points: {total_points} out of 10")
