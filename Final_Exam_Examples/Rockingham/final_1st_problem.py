import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
# Chatgpt was used

def height_vs_time(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t ** 2


data_file = 'Projectile.csv'

time = []
height = []
time_error = []
height_error = []

with open(data_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        time.append(float(row[0]))
        height.append(float(row[1]))
        time_error.append(float(row[2]))
        height_error.append(float(row[3]))

# Perform curve fitting
popt, pcov = curve_fit(height_vs_time, time, height, sigma=height_error, absolute_sigma=True)

# Extract fit parameters and uncertainties
y0_fit = popt[0]
vy0_fit = popt[1]
g_fit = popt[2]

# Calculate fitted values
height_fit = height_vs_time(np.array(time), *popt)

# Plotting
plt.figure(figsize=(10, 6))

# Data points with error bars
plt.errorbar(time, height, xerr=time_error, yerr=height_error, fmt='o', label='Data')

# Fitted curve
plt.plot(time, height_fit, 'r-', label='Fit')

# Labels and title
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height vs Time with Fit')
plt.legend()

# Save and show plot
plt.savefig('height_vs_time_plot.png')
plt.show()
print("Completed")
