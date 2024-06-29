import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# first, define the height function
def height_function(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t ** 2


# reads file name from input
file_name = 'Projectile.csv'

time = []
height = []
time_uncertainty = []
height_uncertainty = []

# This opens and reads the CSV file
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skips the header row
    for row in reader:
        time.append(float(row[0]))
        height.append(float(row[1]))
        time_uncertainty.append(float(row[2]))
        height_uncertainty.append(float(row[3]))

# this next bit converts lists to the numPy arrays for operations
time = np.array(time)
height = np.array(height)
time_uncertainty = np.array(time_uncertainty)
height_uncertainty = np.array(height_uncertainty)

# next, this performs the curve fitting using the height/data with uncertainties
popt, pcov = curve_fit(height_function, time, height, sigma=height_uncertainty, absolute_sigma=True)
y0_fit, vy0_fit, g_fit = popt
y0_uncertainty, vy0_uncertainty, g_uncertainty = np.sqrt(np.diag(pcov))

print(f"y(0) = {y0_fit:.3f} +/- {y0_uncertainty:.3f} meters")
print(f"vy(0) = {vy0_fit:.3f} +/- {vy0_uncertainty:.3f} m/s")
print(f"g = {g_fit:.3f} +/- {g_uncertainty:.3f} m/s^2")

# this checks to see if the extracted value of g agrees with the expected value
expected_g = 9.81
if abs(g_fit - expected_g) <= g_uncertainty:
    print(f"G agrees with {expected_g} m/s^2")
else:
    print(f"G doesn't agree with {expected_g} m/s^2")
print("Completed")

# this plots the data with error bars and fit
plt.errorbar(time, height, yerr=height_uncertainty, xerr=time_uncertainty, fmt='o', label='Data', ecolor='red',
             capsize=5)

# this generates a smooth curve for the fit line
time_fit = np.linspace(min(time), max(time), 100)
height_fit = height_function(time_fit, *popt)
plt.plot(time_fit, height_fit, label='Fit', color='blue')

# this will calculate the 1 sigma error bands
y_fit_upper = height_function(time_fit, y0_fit + y0_uncertainty, vy0_fit + vy0_uncertainty, g_fit + g_uncertainty)
y_fit_lower = height_function(time_fit, y0_fit - y0_uncertainty, vy0_fit - vy0_uncertainty, g_fit - g_uncertainty)

# this fills the area(s) between the upper and lower bounds of fit
plt.fill_between(time_fit, y_fit_lower, y_fit_upper, color='blue', alpha=0.2, label=r'$\pm 1\sigma$ error band')

# finally, this sets the labels and titles of the plot
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.title('Height vs Time with Fit and Error Bands')
plt.show()