import matplotlib.pyplot as plt

# Define the Golden Ratio
phi = (1.0 + 5.0 ** 0.5) / 2.0


# Define a function to calculate f_n for real values of n
def fibonacci_phi(n):
    global phi
    return (phi**n-(-1.0/phi)**n)/5.0**0.5


# Define a function to create a LIST of f_n for a range of real values of n
def fibonacci_list(xlow, xhigh):

    npts = 1111
    dx = (xhigh - xlow) / npts

    x_values = []
    y_values = []

    for i in range(npts):
        x = xlow + i * dx
        fn = fibonacci_phi(x)
        # print(x,fn)
        x_values.append(fn.real)
        y_values.append(fn.imag)

    return x_values, y_values


if __name__ == '__main__':

    # set the ranges for "n" ... so, this will calculate the complex Fibonacci
    # sequence for real values of n between [xlow,xhigh] and [-xhigh,-xlow]
    xlow = 0.0
    xhigh = 5.1

    # create lists that contain the positive and negative Fibonacci sequences for
    # INTEGER values of n, since we know what those numbers are, and can then make
    # comparisons, visually.
    fibonnaci_real_pos = [fibonacci_phi(n) for n in range(int(xlow),int(xhigh)+1)]
    fibonnaci_imag_pos = [0 for n in range(int(xlow),int(xhigh)+1)]
    fibonnaci_real_neg = [fibonacci_phi(n) for n in range(-int(xhigh), -int(xlow)+1)]
    fibonnaci_imag_neg = [0 for n in range(-int(xhigh), -int(xlow)+1)]

    npts = 1111
    dx = (xhigh-xlow)/npts

    x_values_pos, y_values_pos = fibonacci_list(xlow, xhigh)
    x_values_neg, y_values_neg = fibonacci_list(xlow, -xhigh)

    # create a figure that has:
    #       (i) an aspect ratio of 10 inches wide x 6 inches high
    #       (ii) two subplots - one row, two columns
    #       (iii) names for the two subplots - ax1 and ax2
    #       (iv) an appropriate title
    #       (v) padding around each subplot, so that don't overlap with one another
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10, 6))
    fig.suptitle('Complex Fibonacci Sequence')
    fig.tight_layout(pad=2.5)

    # make the left plot
    ax1.plot(x_values_pos, y_values_pos)
    ax1.plot(fibonnaci_real_pos, fibonnaci_imag_pos, 'o')
    # plot vertical horizontal lines to indicate the y- and x-axis.
    ax1.axvline(x=0, c="black", linewidth=0.5)
    ax1.axhline(y=0, c="black", linewidth=0.5)
    # title and axis labels
    ax1.set_title("Positive Sequence")
    ax1.set_xlabel("Real(f_n)")
    ax1.set_ylabel("Imag(f_n)")

    # make the right plot, similar to the left plot
    ax2.plot(x_values_neg, y_values_neg)
    ax2.plot(fibonnaci_real_neg, fibonnaci_imag_neg, 'o')
    ax2.axvline(x=0, c="black", linewidth=0.5)
    ax2.axhline(y=0, c="black", linewidth=0.5)
    ax2.set_title("Negative Sequence")
    ax2.set_xlabel("Real(f_n)")
    ax2.set_ylabel("Imag(f_n)")

    plt.show()
