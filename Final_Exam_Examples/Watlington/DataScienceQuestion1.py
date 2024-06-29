import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def read_data(filename):
    height = []  # height
    time = []  # time
    dheight = []  # error in height
    dtime = []  # error in time

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        for row in reader:
            height.append(float(row[0]))
            time.append(float(row[1]))
            dheight.append(float(row[2]))
            dtime.append(float(row[3]))

    return headers, height, time, dheight, dtime


def fit(x, *param):
    return param[0] * x * x + param[1] * x + param[2]


if __name__ == '__main__':
    file = "Projectile.csv"
    header_values, xi, yi, dxi, dyi = (read_data(file))
    print(header_values)
    print(xi, yi, dxi, dyi)

    plt.errorbar(xi, yi, xerr=dxi, yerr=dyi, fmt='o', label="Time(s)", capsize=5.0)
    plt.title("Height vs Time")
    plt.xlabel(header_values[0])
    plt.ylabel(header_values[1])

    plt.ylim(0)

    popt, pcov = curve_fit(fitfunction, xi, yi, sigma=dyi, absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))


    




print("Completed")