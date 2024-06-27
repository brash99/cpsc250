import numpy as np
import pandas as pd
import scipy.optimize as opt
import matplotlib.pyplot as plt


def read_data(file_path):
    data = pd.read_csv(file_path)
    x = data['Temperature'].values
    y = data['Pollen Count'].values
    dx = data['Error in Temperature'].values
    dy = data['Error in Pollen Count'].values
    return x, y, dx, dy


def quadratic(x, a, b, c):
    return a * x ** 2 + b * x + c


def fit_quadratic(x, y, dy):
    popt, pcov = opt.curve_fit(quadratic, x, y, sigma=dy, absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr, pcov

def main():
    file_path = 'testdata.csv'  # Updated file path
    x, y, dx, dy = read_data(file_path)

    popt, perr, pcov = fit_quadratic(x, y, dy)
    print("Fitted parameters:", popt)
    print("Parameter uncertainties:", perr)
    print("Covariance matrix:", pcov)

    # Plotting the data and the fit
    plt.errorbar(x, y, yerr=dy, xerr=dx, fmt='o', label='Data', capsize=5)
    x_fit = np.linspace(0, max(x)+10, 100)
    y_fit = quadratic(x_fit, *popt)

    # Create the fit label with parameters and uncertainties
    fit_label = (f'Quadratic fit:\n'
                 f'a = {popt[0]:.3f} ± {perr[0]:.3f}\n'
                 f'b = {popt[1]:.3f} ± {perr[1]:.3f}\n'
                 f'c = {popt[2]:.3f} ± {perr[2]:.3f}')

    # Generate parameter samples from the covariance matrix
    n_samples = 1000
    param_samples = np.random.multivariate_normal(popt, pcov, n_samples)

    # Generate fit curves for each sample
    y_fits = np.array([quadratic(x_fit, *params) for params in param_samples])

    # Calculate the confidence interval
    y_fit_lower = np.percentile(y_fits, 2.5, axis=0)
    y_fit_upper = np.percentile(y_fits, 97.5, axis=0)

    plt.plot(x_fit, y_fit, label=fit_label)
    plt.fill_between(x_fit, y_fit_lower, y_fit_upper, color='gray', alpha=0.2, label='Fit uncertainty')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.xlim(0,max(x)+10)
    plt.ylim(0)
    plt.show()


if __name__ == "__main__":
    main()