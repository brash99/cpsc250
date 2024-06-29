import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
def kinemactic_eq(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2
data = pd.read_csv('Projectile.csv')
time = data['time'].values
height = data['height'].values
time_uncertanity = data['time_uncertainity'].values
hieght_uncertainity = data['height_uncertainity'].values
popt, pcov = curve_fit(kinematic_eq, time, height, sigma=height_uncertainty, absolute_sigma=True)
y0, vy0, g = popt
y0_uncertainty, vy0_uncertainty, g_uncertainty = np.sqrt(np.diag(pcov))
print(f"y0 = {y0:.2f} +/- {y0_uncertainty:.2f}")
print(f"vy0 = {vy0:.2f} +/- {vy0_uncertainty:.2f}")
print(f"g = {g:.2f} +/- {g_uncertainty:.2f}")
expected_g = 9.81
if np.abs(g - expected_g) <= g_uncertainty:
    print("The extracted value of g agrees with the expected value.")
else:
    print("The extracted value of g does not agree with the expected value.")
plt.figures((figsize==10,6))
plt.errorbar(time, height, yerr=height_uncertainty, xerr=time_uncertainty, fmt='o', label='Data', ecolor='red', capsize=4)
time_fit = np.linspace(min(time), max(time), 1000)
height_fit = kinematic_eq(time_fit, *popt)
plt.plot(time_fit, height_fit, 'b-', label='Fit')

print("Completed")