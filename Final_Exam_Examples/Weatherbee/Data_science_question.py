import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define the kinematic equation for fitting
def kinematic_equation(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t ** 2


# Attempt to read the CSV file
data_file = 'data.csv'  # Replace with the correct path or filename

try:
    with open(data_file, 'r') as file:
        times = []
        heights = []
        time_uncertainties = []
        height_uncertainties = []

        reader = csv.DictReader(file)
        for row in reader:
            times.append(float(row['time']))
            heights.append(float(row['height']))
            time_uncertainties.append(float(row['time_uncertainty']))
            height_uncertainties.append(float(row['height_uncertainty']))

    # Convert lists to numpy arrays
    times = np.array(times)
    heights = np.array(heights)
    time_uncertainties = np.array(time_uncertainties)
    height_uncertainties = np.array(height_uncertainties)

    # Perform curve fitting
    popt, pcov = curve_fit(kinematic_equation, times, heights, sigma=height_uncertainties)
    y0, vy0, g = popt
    perr = np.sqrt(np.diag(pcov))

    # Extract uncertainties
    # Used chatgpt to help
    y0_uncertainty, vy0_uncertainty, g_uncertainty = perr

    # Print the fit parameters with uncertainties
    print(f"y0 = {y0:.2f} ± {y0_uncertainty:.2f} m")
    print(f"vy0 = {vy0:.2f} ± {vy0_uncertainty:.2f} m/s")
    print(f"g = {g:.2f} ± {g_uncertainty:.2f} m/s^2")

    # Compare extracted g with expected g
    expected_g = 9.81
    if np.abs(g - expected_g) <= g_uncertainty:
        print(f"The extracted value of g agrees with the expected value of {expected_g} m/s^2.")
    else:
        print(f"The extracted value of g disagrees with the expected value of {expected_g} m/s^2.")

    # Plotting the data and the fit
    plt.errorbar(times, heights, yerr=height_uncertainties, xerr=time_uncertainties, fmt='o',
                 label='Data with uncertainties')
    time_fit = np.linspace(min(times), max(times), 500)
    height_fit = kinematic_equation(time_fit, *popt)

    plt.plot(time_fit, height_fit, label='Fit', color='red')

    # Calculate the 1 sigma error bands
    upper_band = kinematic_equation(time_fit, y0 + y0_uncertainty, vy0 + vy0_uncertainty, g - g_uncertainty)
    lower_band = kinematic_equation(time_fit, y0 - y0_uncertainty, vy0 - vy0_uncertainty, g + g_uncertainty)

    plt.fill_between(time_fit, lower_band, upper_band, color='gray', alpha=0.5, label='1 sigma error band')

    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.title('Height vs Time')
    plt.legend()
    plt.show()

    print("Completed")

except FileNotFoundError:
    print(f"Error: File '{data_file}' not found.")
