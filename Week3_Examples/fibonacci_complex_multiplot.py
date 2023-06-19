import matplotlib.pyplot as plt

phi = (1.0 + 5.0 ** 0.5) / 2.0


def fibonacci_phi(n):
    global phi
    return (phi**n-(-1.0/phi)**n)/5.0**0.5


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

    xhigh = 5.1

    fibonnaci_real_pos = [fibonacci_phi(n) for n in range(int(xhigh)+1)]
    fibonnaci_imag_pos = [0 for n in range(int(xhigh)+1)]
    fibonnaci_real_neg = [fibonacci_phi(n) for n in range(-int(xhigh), 1)]
    fibonnaci_imag_neg = [0 for n in range(-int(xhigh), 1)]

    xlow = 0.0

    npts = 1111
    dx = (xhigh-xlow)/npts

    x_values_pos, y_values_pos = fibonacci_list(xlow, xhigh)
    x_values_neg, y_values_neg = fibonacci_list(xlow, -xhigh)

    fig, axs = plt.subplots(2,  figsize=(6, 9))
    fig.suptitle('Complex Fibonacci Sequence')
    fig.tight_layout(pad=3.5)

    axs[0].plot(x_values_pos, y_values_pos)
    axs[0].plot(fibonnaci_real_pos, fibonnaci_imag_pos, 'o')
    axs[0].axvline(x=0, c="black", linewidth=0.5)
    axs[0].axhline(y=0, c="black", linewidth=0.5)
    axs[0].set_title("Positive Sequence")
    axs[0].set_xlabel("Real(f_n)")
    axs[0].set_ylabel("Imag(f_n)")

    axs[1].plot(x_values_neg, y_values_neg)
    axs[1].plot(fibonnaci_real_neg, fibonnaci_imag_neg, 'o')
    axs[1].axvline(x=0, c="black", linewidth=0.5)
    axs[1].axhline(y=0, c="black", linewidth=0.5)
    axs[1].set_title("Negative Sequence")
    axs[1].set_xlabel("Real(f_n)")
    axs[1].set_ylabel("Imag(f_n)")

    plt.show()
