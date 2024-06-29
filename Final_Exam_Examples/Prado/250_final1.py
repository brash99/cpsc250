import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Define the kinematic function
def kinematic_function(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2

# File path
file_path = r'C:\Users\blake\PycharmProjects\cpsc250\Tests\Projectile.csv'

time = []
height = []

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        time.append(float(row['Time']))
        height.append(float(row['Height']))

# Convert lists to numpy arrays
time = np.array(time)
height = np.array(height)

# Perform curve fitting
popt, pcov = curve_fit(kinematic_function, time, height)
y0, vy0, g = popt

# Create the plot without error band
plt.plot(time, height, 'o', label='Data')  # Plotting data points without error bars

# Plot the fit
time_fit = np.linspace(min(time), max(time), 500)
height_fit = kinematic_function(time_fit, *popt)
plt.plot(time_fit, height_fit, label='Fit')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.show()

# Report the values
print(f'y(0) = {y0:.4f} meters')
print(f'vy(0) = {vy0:.4f} m/s')
print(f'g = {g:.4f} m/s^2')
