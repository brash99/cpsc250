"""The following program is intended to read in the data from Projectile.csv,
which should contain the time, height, error in time measurement, and error in height measurement
for a kinematics experiment.
The program then fits this data to the basic kinematics equation height = y(0) + vy(0) t - g/2 t^2,
assesses and reports on if the calculated value of g falls within the uncertainty,
and creates a plot of "height" vs "time" that shows the data, with error bars, along with the fit to the data,
including +/- 1 sigma error bands.
The program was created with the help of ChatGPT and with substantial references to basic_data_plotting_exp.py."""

import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

'''Function read_data(filename) is based on read_data(filename) from basic_data_plotting_exp.py'''
'''Given a file name, the function reads in four columns of data'''
'''and stores them in the lists time, height, time_err, and height_err.'''
'''The function then returns the headers and the columns of data as lists.'''


def read_data(filename):
    time = []
    height = []
    time_err = []
    height_err = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Read headers
        for row in reader:
            time.append(float(row[0]))        # Append time data
            height.append(float(row[1]))      # Append height data
            time_err.append(float(row[2]))    # Append time error data
            height_err.append(float(row[3]))  # Append height error data

    return headers, time, height, time_err, height_err


'''Function fitfunction(t, g, vy0, y0) enables fitting the data
to the kinematics equation height = y(0) + vy(0) t - g/2 t^2'''


def fitfunction(t, g, vy0, y0):
    return -0.5 * g * t ** 2 + vy0 * t + y0


if __name__ == '__main__':
    # Step 1: Read in the CSV file into appropriate data structures
    file_name = "Projectile.csv"
    header_values, time, height, time_err, height_err = read_data(file_name)

    # Step 2: Perform a fit to the data using a fitting function corresponding to the kinematics equation
    # using weighted least squares and initial values based on the data and standard value for g
    init_vals = [1.0, 10.0, 9.81]
    popt, pcov = curve_fit(fitfunction, time, height, p0=init_vals, sigma=height_err, absolute_sigma=True)

    # Step 3a: Extract the fit parameters with uncertainties
    g_fit, vy0_fit, y0_fit = popt
    g_err, vy0_err, y0_err = np.sqrt(np.diag(pcov))

    # Step 3b: Report the value of each of the parameters +/- uncertainty
    print(f'Fit Result:')
    print(f'g = {g_fit:.2f} +/- {g_err:.2f}')
    print(f'vy(0) = {vy0_fit:.2f} +/- {vy0_err:.2f}')
    print(f'y(0) = {y0_fit:.2f} +/- {y0_err:.2f}')

    # Step 4: Create a plot of "height" vs "time" that shows the data, with error bars,
    # along with the fit to the data,including +/- 1 sigma error bands
    plt.title("Projectile Motion Experiment")
    # Label x-axis with the first header value (time)
    plt.xlabel(header_values[0])
    # Label y-axis with the second header value (height)
    plt.ylabel(header_values[1])
    # Plot data as dots with error bars for both time and height as in the example figure
    plt.errorbar(time, height, xerr=time_err, yerr=height_err, fmt='o', label="Data", capsize=5.0)
    # Extend the y-axis minimum to -1 and the maximum to 11 as in the example figure
    plt.ylim(-1, max(height) + 1)
    # Extend the x-axis minimum to -0.2 and the maximum to 2.7 as in the example figure
    plt.xlim(-0.2, max(time) + 0.2)
    # Show grid lines for x = 0 and y = 0 as in the example figure
    plt.gca().axhline(0, color='black', linewidth=0.5)  # Horizontal line at y = 0
    plt.gca().axvline(0, color='black', linewidth=0.5)  # Vertical line at x = 0
    # Output the fit for the data points, extended by 0.1 seconds on each side as in the example figure
    t_fit = np.linspace(min(time) - 0.1, max(time) + 0.1, 100)
    height_fit = fitfunction(t_fit, *popt)
    # Plot fit as red dashed line as in example figure
    # Label fit
    plt.plot(t_fit, height_fit, 'r--', label=f"Quadratic Fit:\n"
                                             f"y = -0.5*({g_fit:.2f} +/- {g_err:.2f})t^2 +\n"
                                             f"({vy0_fit:.2f} +/- {vy0_err:.2f})t +\n"
                                             f"({y0_fit:.2f} +/- {y0_err:.2f})")
    # Plot the +/- 1 sigma error lines as green dashed lines as in the example figure
    t_range = np.linspace(min(time) - 0.1, max(time) + 0.1, 100)  # Extend range by 1 unit on each side
    y_fit_upper = fitfunction(t_range, g_fit + g_err, vy0_fit + vy0_err, y0_fit + y0_err)
    y_fit_lower = fitfunction(t_range, g_fit - g_err, vy0_fit - vy0_err, y0_fit - y0_err)
    plt.plot(t_range, y_fit_upper, 'g--', label='One Sigma Error', linewidth=1.0)
    plt.plot(t_range, y_fit_lower, 'g--', linewidth=1.0)
    # Display legend in lower right hand corner
    plt.legend(loc='lower right')
    # Adjust parameters so the axes fit the figure area
    plt.tight_layout()
    # Show the final figure
    plt.show()

    # Step 5: Calculate and report on whether the extracted value of "g"
    # agrees or disagrees with the expected value (9.81 m/s^2)
    expected_g = 9.81
    g_min = g_fit - g_err
    g_max = g_fit + g_err
    print(f'Extracted value of g: {g_fit:.2f} +/- {g_err:.2f} m/s^2')
    print(f'Expected value of g: {expected_g} m/s^2')
    if g_min <= expected_g <= g_max:
        print('The extracted value of g agrees with the expected value within the uncertainty range.')
    else:
        print('The extracted value of g disagrees with the expected value outside the uncertainty range.')
