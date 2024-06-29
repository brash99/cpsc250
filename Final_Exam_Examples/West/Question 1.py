import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

# reading data
data = pd.read_csv('Projectile.csv')
# creating kinematics function i used chat gpt to help me make this
def kinematics_calculation(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2
# assigning variables to the data I used chat gpt to help me write this 
time = data['Time']
height = data['Height']
dtime = data['dTime']
dheight = data['dHeight']
# fitting the curve, i used chat gpt to help me write this
popt, pcov = curve_fit(kinematics_calculation, time, height, sigma=dheight, absolute_sigma=True)
y0, vy0, g = popt
dy0, dvy0, dg = np.sqrt(np.diag(pcov))
# generating data
fitted_height = kinematics_calculation(time, *popt)
# Create the plot I used chat gpt to help me write this code
plt.figure(figsize=(10, 6))
plt.errorbar(time, height, yerr=dheight, fmt='o', label='Data', ecolor='red', capsize=5)
plt.plot(time, fitted_height, label='Fit', color='blue')
plt.fill_between(time, fitted_height - dheight, fitted_height + dheight, color='blue', alpha=0.2, label='1 sigma error band')


# adding labels and title, i used chat gpt for this
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height vs Time with Fit')
plt.legend()

plt.show()
# printing the results, i used chat gpt to write this
print(f"y0 = {y0:.3f} +/- {dy0:.3f}")
print(f"vy0 = {vy0:.3f} +/- {dvy0:.3f}")
print(f"g = {g:.3f} +/- {dg:.3f}")

#checking g value
expected_num = 9.81
if abs(g - expected_num) <= dg:
    print("Agrees")
else:
    print("Disagree\'s")