import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Define the model function, returns formula.
def model(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2

# Reads the CSV file
with open('Projectile.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Convert data(time and Height) to numpy arrays
t = np.array([float(row['Time']) for row in data])
h = np.array([float(row['Height']) for row in data])

# Perform the fit
popt, pcov = curve_fit(model, t, h)
perr = np.sqrt(np.diag(pcov))

# Extracts the variables and the prints are for testing, not needed.
y0, vy0, g = popt
#print(f'y(0) = {y0:.2f} ± {perr[0]:.2f}')
#print(f'vy(0) = {vy0:.2f} ± {perr[1]:.2f}')
#print(f'g = {g:.2f} ± {perr[2]:.2f}')

# Creates the plot with a legend, fit, and x and y labels.
plt.scatter(t, h, label='Data')
t_fit = np.linspace(min(t), max(t), 1000)
h_fit = model(t_fit, *popt)
plt.plot(t_fit, h_fit, 'r-', label='Fit')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.show()

# print completed
print("Completed")
