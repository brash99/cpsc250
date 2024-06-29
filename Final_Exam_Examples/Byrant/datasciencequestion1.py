import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read CSV file
try:
    data = pd.read_csv('Projectile.csv')
except FileNotFoundError:
    print("Error: CSV file 'Projectile.csv' not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: CSV file 'Projectile.csv' is empty.")
    exit(1)
except pd.errors.ParserError:
    print("Error: Parsing error occurred with CSV file 'Projectile.csv'.")
    exit(1)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Check if expected columns exist
expected_columns = ['time', 'height', 'time_uncertainty', 'height_uncertainty']
missing_columns = [col for col in expected_columns if col not in data.columns]
if missing_columns:
    print(f"Error: Missing columns in CSV file: {', '.join(missing_columns)}")
    exit(1)

# Extract data columns
time = data['time'].values
height = data['height'].values
time_uncertainty = data['time_uncertainty'].values
height_uncertainty = data['height_uncertainty'].values

# Define the fitting function
def height_function(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2

# Initial guess for parameters (can be improved based on knowledge or initial inspection)
initial_guess = (1.0, 1.0, 10.0)

# Perform curve fitting
try:
    params, cov_matrix = curve_fit(height_function, time, height, p0=initial_guess, sigma=height_uncertainty)
except RuntimeError as e:
    print(f"Error: Curve fitting failed. {e}")
    exit(1)

# Extract fit parameters and their uncertainties
y0_fit, vy0_fit, g_fit = params
errors = np.sqrt(np.diag(cov_matrix))
error_y0, error_vy0, error_g = errors

# Plotting the data with error bars
plt.figure(figsize=(10, 6))
plt.errorbar(time, height, xerr=time_uncertainty, yerr=height_uncertainty, fmt='o', label='Experimental Data')

# Plot the fitted curve
t_fit = np.linspace(min(time), max(time), 100)
height_fit = height_function(t_fit, *params)
plt.plot(t_fit, height_fit, label='Fit: $y(0) + vy(0) t - g/2 t^2$')

# Plot ±1 sigma error bands
height_upper = height_function(t_fit, y0_fit + error_y0, vy0_fit + error_vy0, g_fit + error_g)
height_lower = height_function(t_fit, y0_fit - error_y0, vy0_fit - error_vy0, g_fit - error_g)
plt.fill_between(t_fit, height_lower, height_upper, alpha=0.2, label='$\pm 1\sigma$ Error')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion Experiment')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

# Compare g_fit with expected value of g = 9.81 m/s^2
expected_g = 9.81
print(f"Extracted value of g: {g_fit:.2f} ± {error_g:.2f} m/s^2")
print(f"Expected value of g: {expected_g} m/s^2")
if np.abs(g_fit - expected_g) < error_g:
    print("The extracted value of g agrees with the expected value within uncertainty.")
else:
    print("The extracted value of g does not agree with the expected value within uncertainty.")

# If everything runs smoothly, print "Completed"
print("Completed")