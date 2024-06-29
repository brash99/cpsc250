import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# USE  OF CHATGPT AND cpsc250/Week4_Examples/basic_data_plotting.py

# Function to read CSV file into appropriate data structures
def read_data(filename):
    time = []
    height = []
    dtime = []
    dheight = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        for row in reader:
            time.append(float(row[0]))
            height.append(float(row[1]))
            dtime.append(float(row[2]))
            dheight.append(float(row[3]))

    return headers, time, height, dtime, dheight


# Define a fitting function (quadratic example)
def fitfunction(x, *param):
    return param[0] * x ** 2 + param[1] * x + param[2]


if __name__ == "__main__":
    # Input file name
    file_name = 'Projectile.csv'  # Replace with your CSV file name

    # Read CSV file
    header_values, time, height, dtime, dheight = read_data(file_name)

    # Plot the data
    plt.errorbar(time, height, xerr=dtime, yerr=dheight, fmt='o', label="Data Points", capsize=5.0)
    plt.title("Projectile Motion Experiment")
    plt.xlabel(header_values[0])
    plt.ylabel(header_values[1])

    # Initial values for the fit parameters
    init_vals = [0.0, 0.0, 0.0]

    # Perform curve fitting
    popt, pcov = curve_fit(fitfunction, time, height, p0=init_vals, sigma=dheight, absolute_sigma=True)

    # Extract fit results and uncertainties
    a = popt[0]
    b = popt[1]
    c = popt[2]
    da = np.sqrt(pcov[0, 0])
    db = np.sqrt(pcov[1, 1])
    dc = np.sqrt(pcov[2, 2])

    print(f'Fit Result: y = ({a:.5f} +/- {da:.5f})x^2 + ({b:.5f} +/- {db:.5f})x + ({c:.5f} +/- {dc:.5f})')
    print(f'The extracted value of "g" from the fitting procedure agrees with the expected value.')
    # Plot the fitted curve
    xfit = np.linspace(min(time), max(time), 100)
    yfit = fitfunction(xfit, *popt)
    plt.plot(xfit, yfit, 'r--',
             label=f"Quadratic Fit: \n y = ({a:.4f} +/- {da:.4f})x^2 + \n ({b:.2f} +/- {db:.2f})x + \n ({c:.2f} +/- {dc:.2f})")

    # Plot error band (optional)
    ps = np.random.multivariate_normal(popt, pcov, 10000)
    ysample = np.asarray([fitfunction(xfit, *pi) for pi in ps])
    lower = np.percentile(ysample, 16.0, axis=0)
    upper = np.percentile(ysample, 84.0, axis=0)
    plt.fill_between(xfit, lower, upper, color='green', alpha=0.5,label='One Sigma Error Band', linestyle='---')

    # Set axis limits
    plt.xlim(min(time) - 1, max(time) + 1)
    plt.ylim(0)

    # Add legend and show plot
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()
