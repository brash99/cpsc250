import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def read_data(filename):
    x = []
    y = []
    dx = []
    dy = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
            dx.append(float(row[2]))
            dy.append(float(row[3]))

    return headers, x, y, dx, dy


# Step 3a: Define a quadratic fit function
def fitfunction(x, *param):
    return param[0]*x*x + param[1]*x + param[2]


# Step 3a: Define an exponential+bkgd fit function
def expfunction(x, *param):
    return param[0]*np.exp(param[1]*x) + param[2]


if __name__ == '__main__':

    # Step 1:  Read the data into appropriate data structures
    file_name = "testdata.csv"
    header_values, xi, yi, dxi, dyi = read_data(file_name)

    # print(header_values)
    # print(xi, yi, dxi, dyi)

    # Step 2: Basic plot of the data with error bars, plot title, and axis labels
    plt.errorbar(xi, yi, xerr=dxi, yerr=dyi, fmt='o', label="Pollen Count Data", capsize=5.0)
    plt.title("Basic Plotting Example")
    plt.xlabel(header_values[0])
    plt.ylabel(header_values[1])

    # Make sure lower limit of y-axis is zero!
    plt.ylim(0)
    plt.xlim(0)

    # Possibly, choose logarithmic x and/or y scales.
    # plt.xscale('log')
    # plt.yscale('log')

    fitchoice = 2

    if fitchoice == 1:
        # Step 3b:  Fit the data with quadratic
        init_vals = [0 for x in range(3)]
        popt, pcov = curve_fit(fitfunction, xi, yi, p0=init_vals, sigma=dyi, absolute_sigma=True)
    else:
        # Step 3b:  Fit the data with exponential + background
        init_vals = [1.0, 0.01, 10.00]  # N.B. need to choose initial guesses that make sense!!!
        popt, pcov = curve_fit(expfunction, xi, yi, p0=init_vals, sigma=dyi, absolute_sigma=True)

    # print(popt)
    # print(perr)
    # print(pcov)

    # Step 3c:  Extract the fit parameters, with uncertainties
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

    # Step 3d:  Plot the fit result
    xlow = min(xi) - 30
    xhigh = max(xi) + 10
    xfit = np.linspace(xlow, xhigh, 100)

    if fitchoice == 1:
        yfit = fitfunction(xfit, *popt)
        plt.plot(xfit, yfit, 'r--', label=f"Quadratic Fit: \ny = ({a:.4f} +/- {da:.4f})x^2 + \n({b:.2f} +/- {db:.2f})x + \n({c:.2f} +/- {dc:.2f})")

    else:
        yfit = expfunction(xfit, *popt)
        #plt.plot(xfit, yfit, 'r--', label=f"Exponential Fit: \ny = ({a:.4f} +/- {da:.4f})e^(({b:.3f} +/- {db:.3f})x) + \n({c:.2f} +/- {dc:.2f})")

    # Step 4:  Plot the error band

    plot_error_band = True

    if plot_error_band:
        ps = np.random.multivariate_normal(popt, pcov, 10000)
        if fitchoice == 1:
            ysample = np.asarray([fitfunction(xfit, *pi) for pi in ps])
        else:
            ysample = np.asarray([expfunction(xfit, *pi) for pi in ps])

        lower = np.percentile(ysample, 16.0, axis=0)
        upper = np.percentile(ysample, 84.0, axis=0)
        middle = (upper+lower)/2.0
        plt.plot(xfit, upper, 'g--', label='One Sigma Error Band')
        plt.plot(xfit, lower, 'g--')
        if fitchoice == 2:
            plt.plot(xfit, middle, 'r--', label=f"Exponential Fit: \ny = ({a:.4f} +/- {da:.4f})e^(({b:.3f} +/- {db:.3f})x) + \n({c:.2f} +/- {dc:.2f})")

    plt.legend()

    # Calculate Goodness of Fit:
    if fitchoice == 1:
        yfit2 = fitfunction(np.array(xi), *popt)
    else:
        yfit2 = expfunction(np.array(xi), *popt)

    chi2 = 0.0
    for i in range(len(xi)):
        # print(yi[i],yfit2[i],dyi[i])
        chi2 += (yi[i]-yfit2[i])**2/dyi[i]**2

    print(f"Goodness of Fit (reduced chi^2) = {chi2/(len(xi)-1-len(init_vals))}")

    plt.show()
