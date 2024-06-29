import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# Define the kinematic equation
def kinematic_eq(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2


# Prompt for the CSV file name
file_name = 'Projectile.csv'

try:
    # Load the data from the CSV file
    data = np.genfromtxt(file_name, delimiter='\t', skip_header=1)
    if data.shape[1] != 4:
        raise ValueError("The input file must have exactly 4 columns: Time, Height, dTime, and dHeight.")
    time = data[:, 0]
    height = data[:, 1]
    dtime = data[:, 2]
    d_height = data[:, 3]

    # Perform curve fitting
    popt, p_cov = curve_fit(kinematic_eq, time, height,  sigma=d_height, absolute_sigma=True)

    # Extract fit parameters and uncertainties
    y0_fit, vy0_fit, g_fit = popt
    y0_err, vy0_err, g_err = np.sqrt(np.diag(p_cov))

    # Print the fit parameters with uncertainties
    print(f"y0 = {y0_fit:.2f} ± {y0_err:.2f}")
    print(f"vy0 = {vy0_fit:.2f} ± {vy0_err:.2f}")
    print(f"g = {g_fit:.2f} ± {g_err:.2f}")

    # Check if extracted g agrees with 9.81 m/s^2
    if np.isclose(g_fit, 9.81, atol=g_err):
        print(f"The extracted value of g ({g_fit:.2f} ± {g_err:.2f}) agrees with the expected value of 9.81 m/s².")
    else:
        print(f"The extracted value of g ({g_fit:.2f} ± {g_err:.2f}) "
              f"does not agree with the expected value of 9.81 m/s².")

    # Create a plot of "height" vs "time"
    plt.errorbar(time, height, yerr=d_height, xerr=dtime, fmt='o', label='Data with error bars')

    # Generate fitted curve
    time_fit = np.linspace(np.min(time), np.max(time), 500)
    height_fit = kinematic_eq(time_fit, *popt)

    # Generate ±1 sigma error bands
    curve_upper = kinematic_eq(time_fit, y0_fit + y0_err, vy0_fit + vy0_err, g_fit + g_err)
    curve_lower = kinematic_eq(time_fit, y0_fit - y0_err, vy0_fit - vy0_err, g_fit - g_err)

    plt.plot(time_fit, height_fit, 'r-', label='Fit')
    plt.fill_between(time_fit, curve_lower, curve_upper, color='red', alpha=0.2, label='±1 sigma error band')

    # Labels and legend
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.title('Height vs Time with Fit and Error Bands')
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
