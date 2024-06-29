import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # This is a workaround for MacOS bug
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def kinematic_eq(t,y0,vy0,g):
    return y0 + vy0*t - 0.5*g*t**2

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
def fitfunction(x, *param):
    return param[0]*x*x + param[1]*x + param[2]

def expfunction(x, *param):
    return param[0]*np.exp(param[1]*x) + param[2]

if __name__ == '__main__':

    # Step 1:  Read the data into appropriate data structures
    file_name = "Projectile.csv"
    header_values, xi, yi, dxi, dyi = read_data(file_name)

    # Step 2: Basic plot of the data with error bars, plot title, and axis labels
    plt.errorbar(xi, yi, xerr=dxi, yerr=dyi, fmt='o', label="Data", capsize=5.0)
    plt.title("Projectile Motion Experiment")
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")

    # Make sure lower limit of y-axis is zero!
    plt.ylim(0)
    plt.xlim(0)

    fitchoice = 1

    if fitchoice == 1:
        # Step 3b:  Fit the data with quadratic
        init_vals = [0 for x in range(3)]
        popt, pcov = curve_fit(fitfunction, xi, yi, p0=init_vals, sigma=dyi, absolute_sigma=True)
    else:
        # Step 3b:  Fit the data with exponential + background
        init_vals = [1.0, 0.01, 10.00]  # N.B. need to choose initial guesses that make sense!!!
        popt, pcov = curve_fit(expfunction, xi, yi, p0=init_vals, sigma=dyi, absolute_sigma=True)

    perr = np.sqrt(np.diag(pcov))
    a = popt[0]
    b = popt[1]
    c = popt[2]
    da = perr[0]
    db = perr[1]
    dc = perr[2]
    if fitchoice == 1:
        print(f'Fit Result: y = ({a:.5f} +/- {da:.5f})x^2 + ({b:.5f} +/- {db:.5f})x + ({c:.5f} +/- {dc:.5f})')
    else:
        print(f'Fit Result: y = ({a:.5f} +/- {da:.5f})e(({b:.5f} +/- {db:.5f})x) + ({c:.5f} +/- {dc:.5f})')
    x_fit = np.linspace(min(xi), max(xi), 100)
    y_fit = fitfunction(x_fit, a, b, c)
    plt.plot(x_fit, y_fit,'r--',label=f"Quadratic Fit: \ny = ({a:.4f} +/- {da:.4f})x^2 + \n({b:.2f} +/- {db:.2f})x + \n({c:.2f} +/- {dc:.2f})")
    plot_error_band = True

    if plot_error_band:
        ps = np.random.multivariate_normal(popt, pcov, 10000)
        if fitchoice == 1:
            ysample = np.asarray([fitfunction(x_fit, *pi) for pi in ps])
        else:
            ysample = np.asarray([expfunction(x_fit, *pi) for pi in ps])

        lower = np.percentile(ysample, 16.0, axis=0)
        upper = np.percentile(ysample, 84.0, axis=0)
        middle = (upper + lower) / 2.0
        plt.plot(x_fit, upper, 'g--', label='One Sigma Error Band')
        plt.plot(x_fit, lower, 'g--')

    plt.legend()
    plt.show()
