import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Function to model the kinematic equation
def kinematic_model(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2

# Prompt for the CSV file name
file_name = 'Projectile.csv'

time = []
height = []
time_uncertainty = []
height_uncertainty = []

# Read the CSV file
with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        time.append(float(row['Time']))
        height.append(float(row['Height']))
        time_uncertainty.append(float(row['dTime']))
        height_uncertainty.append(float(row['dHeight']))

# Convert lists to numpy arrays
time = np.array(time)
height = np.array(height)
time_uncertainty = np.array(time_uncertainty)
height_uncertainty = np.array(height_uncertainty)

# Perform curve fitting
popt, pcov = curve_fit(kinematic_model, time, height, sigma=height_uncertainty)
y0_fit, vy0_fit, g_fit = popt
y0_uncertainty, vy0_uncertainty, g_uncertainty = np.sqrt(np.diag(pcov))

# Print fit parameters with uncertainties
print(f"y(0) = {y0_fit:.2f} +/- {y0_uncertainty:.2f} meters")
print(f"vy(0) = {vy0_fit:.2f} +/- {vy0_uncertainty:.2f} m/s")
print(f"g = {g_fit:.2f} +/- {g_uncertainty:.2f} m/s^2")

# Check if extracted g agrees with expected value
g_expected = 9.81
if np.abs(g_fit - g_expected) <= g_uncertainty:
    print(f"The extracted value of g ({g_fit:.2f} +/- {g_uncertainty:.2f}) agrees with the expected value of {g_expected} m/s^2.")
else:
    print(f"The extracted value of g ({g_fit:.2f} +/- {g_uncertainty:.2f}) does not agree with the expected value of {g_expected} m/s^2.")

# Create plot
plt.errorbar(time, height, yerr=height_uncertainty, xerr=time_uncertainty, fmt='o', label='Data')

# Plot the fit
t_fit = np.linspace(min(time), max(time), 100)
height_fit = kinematic_model(t_fit, *popt)
plt.plot(t_fit, height_fit, label='Fit')

# Plot ±1 sigma error bands
upper_bound = kinematic_model(t_fit, y0_fit + y0_uncertainty, vy0_fit + vy0_uncertainty, g_fit + g_uncertainty)
lower_bound = kinematic_model(t_fit, y0_fit - y0_uncertainty, vy0_fit - vy0_uncertainty, g_fit - g_uncertainty)
plt.fill_between(t_fit, lower_bound, upper_bound, color='gray', alpha=0.2, label='1 sigma error band')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height vs Time')
plt.legend()
plt.grid(True)
plt.savefig('height_vs_time_fit.png')
plt.show()

