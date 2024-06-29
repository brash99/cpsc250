import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#Step 1:
#Read in the CSV file into appropriate data structures.
def read_data(filename):
    Time = []
    Height = []
    dTime = []
    dHeight = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            Time.append(float(row[0]))
            Height.append(float(row[1]))
            dTime.append(float(row[2]))
            dHeight.append(float(row[3]))
    return headers, Time, Height, dTime, dHeight



#Step 2:
#Perform a fit to the data using a fitting function that corresponds to the expected behavior, as given in the equation above.
def height_vs_time(t, y0, vy0, g):
    return y0 + vy0 * t - 0.5 * g * t**2
#plot data with error bars
if __name__ == '__main__':
    file_name = "Projectile.csv"
    header_values, Time_data, Height_data, dTime_data, dHeight_data = read_data(file_name)

    plt.errorbar(Time_data, Height_data, xerr=dTime_data, yerr=dHeight_data, fmt='o', label='Data', capsize=5)
    plt.title("Projectile Motion Environment")
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")


#Step3: curve fitting
#Extract uncertainties in the fit parameters, and report the value of each of the parameters +/- uncertainty.
initial_height = [Height_data[0], 5.0, 9.0]
params, cov_matrix = curve_fit(height_vs_time, Time_data, Height_data, p0=initial_height, sigma=dHeight_data, absolute_sigma=True)
#extracting uncertainities
fit_y0, fit_vy0, fit_g = params
uncertainty_y0, uncertainty_vy0, uncertainty_g = np.sqrt(np.diag(cov_matrix))


#Step 4: plot
#time array #come back to this
t_fit = np.linspace(min(Time_data), max(Time_data), 100)
height_fit = height_vs_time(t_fit, fit_y0, fit_vy0, fit_g)
plt.plot(t_fit, height_fit, 'r--', label=f'Quadratic Fit: y = -0.5*({fit_g:.2f} ± {uncertainty_g:.2f})t^2 + ({fit_vy0:.2f} ± {uncertainty_vy0:.2f})t + ({fit_y0:.2f} ± {uncertainty_y0:.2f})')

fit_lower = height_vs_time(t_fit, fit_y0 - uncertainty_y0, fit_vy0 - uncertainty_vy0, fit_g - uncertainty_g)
fit_upper = height_vs_time(t_fit, fit_y0 - uncertainty_y0, fit_vy0 + uncertainty_vy0, fit_g + uncertainty_g)
plt.fill_between(t_fit, fit_lower, fit_upper, color='green', linestyle='--', alpha=0.5, label='One Sigma Error')

#Report on whether the extracted value of "g" from the fitting procedure agrees or disagrees with the expected value.

g_expected = 9.81
if np.isclose(fit_g, g_expected, atol=0.1):
    print("The extracted value of g agrees with the expected value.")
else:
    print("The extracted value of g does not agree with the expected value.")

print("Completed")

plt.legend()
plt.grid(True)
plt.show()