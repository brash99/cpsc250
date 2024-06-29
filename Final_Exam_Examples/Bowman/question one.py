import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# gravitational constant
g_expected = 9.81

# height based on the kinematic equation
def height_model(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2

# CSV file and extract data
filename = 'Projectile.csv'

t_data = []
height_data = []
delta_t_data = []
delta_height_data = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        t_data.append(float(row[0]))
        height_data.append(float(row[1]))
        delta_t_data.append(float(row[2]))
        delta_height_data.append(float(row[3]))

t_data = np.array(t_data)
height_data = np.array(height_data)
delta_t_data = np.array(delta_t_data)
delta_height_data = np.array(delta_height_data)

# create the curve fitting
popt, pcov = curve_fit(height_model, t_data, height_data, sigma=delta_height_data, absolute_sigma=True)

# parameters and uncertainties
y0_fit, vy0_fit, g_fit = popt
y0_err, vy0_err, g_err = np.sqrt(np.diag(pcov))

# make the plot and fit of the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(t_data, height_data, yerr=delta_height_data, xerr=delta_t_data, fmt='o', label='Data')

t_fit = np.linspace(min(t_data), max(t_data), 100)
height_fit = height_model(t_fit, y0_fit, vy0_fit, g_fit)
ax.plot(t_fit, height_fit, 'r-', label='Fit')

# Formulas for 1 sigma error bands
height_upper = height_model(t_fit, y0_fit + y0_err, vy0_fit + vy0_err, g_fit + g_err)
height_lower = height_model(t_fit, y0_fit - y0_err, vy0_fit - vy0_err, g_fit - g_err)
ax.fill_between(t_fit, height_lower, height_upper, color='orange', alpha=0.2, label='$\pm$ 1$\sigma$')

# this is the code for the plot settings
ax.set_xlabel('Time (s)')
ax.set_ylabel('Height (m)')
ax.set_title('Height vs. Time with Fit')
ax.legend()
ax.grid(True)

# plot and save
plt.savefig('height_vs_time_fit.png')
plt.show()

# g_fit compared to expected value
tolerance = 0.1

if abs(g_fit - g_expected) < tolerance:
    print(f"g_fit = {g_fit:.2f} +/- {g_err:.2f} m/s^2 agrees with expected g = {g_expected} m/s^2")
else:
    print(f"g_fit = {g_fit:.2f} +/- {g_err:.2f} m/s^2 disagrees with expected g = {g_expected} m/s^2")

print("Completed")
