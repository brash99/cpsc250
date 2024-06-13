import random

# Look for a file called gv_die.py IN THE SAME DIRECTORY AS THIS FILE
import gv_die

if __name__ == "__main__":

    seed = int(input("Enter the random number generator seed:"))
    random.seed(seed) # Seed the random number generator ... call the seed function of the random module

    number_of_rolls = int(input("Enter the number of rolls:"))

    die = gv_die.GVDie() # Create an instance of the GVDie class ... call the GVDie class constructor within in the gv_die module

    sum_of_rolls = 0
    average = 0

    for i in range(number_of_rolls):
        die.roll()
        print(die.get_value())
        sum_of_rolls += die.get_value()
        average = sum_of_rolls/(i+1)
        print(f"Running average: {average:.2f}")

    print(f"Final average: {average:.2f}")

