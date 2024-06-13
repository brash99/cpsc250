import random
import gv_die

if __name__ == "__main__":

    seed = int(input("Enter the random number generator seed:"))
    random.seed(int(seed))

    number_of_rolls = int(input("Enter the number of rolls:"))

    die = gv_die.GVDie()

    sum_of_rolls = 0
    average = 0

    # create some empty lists to store the values we want to plot
    roll_values = [] # this will be the y-axis for the roll values
    average_values = [] # this will be the y-axis for the average values
    roll_number = [] # this will be the x-axis

    for i in range(number_of_rolls):
        die.roll()
        sum_of_rolls += die.get_value()
        average = sum_of_rolls/(i+1)

        roll_values.append(die.get_value())
        average_values.append(average)
        roll_number.append(i+1)

    print(f"Final average: {average:.2f}")

    import matplotlib.pyplot as plt

    plt.plot(roll_number, roll_values, '.', label='Roll Value')
    plt.plot(roll_number, average_values, label='Average Value')
    plt.xlabel('Roll Number')
    plt.ylabel('Roll Value / Running Average')
    plt.title('Die Roll Average')
    plt.legend()
    plt.show()

