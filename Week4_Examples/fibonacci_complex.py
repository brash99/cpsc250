import matplotlib.pyplot as plt

phi = (1.0 + 5.0**0.5) / 2.0

def fibonacci_phi(n):
    global phi
    return (phi**n-(-1.0/phi)**n)/5.0**0.5


if __name__ == '__main__':

    xlow = 0.0
    xhigh = 5.1
    npts = 1111
    dx = (xhigh-xlow)/npts

    fibonnaci_real_pos = [fibonacci_phi(n) for n in range(int(xhigh)+1)]
    fibonnaci_imag_pos = [0 for n in range(int(xhigh)+1)]

    fibonnaci_real_neg = [fibonacci_phi(n) for n in range(int(xhigh),1)]
    fibonnaci_imag_neg = [0 for n in range(int(xhigh),1)]

    x_values = []
    y_values = []

    for i in range(npts):
        n = xlow + i*dx
        fn = fibonacci_phi(n)
        # print(x,fn)
        x_values.append(fn.real)
        y_values.append(fn.imag)

    plt.plot(x_values, y_values, label="Complex Fibonacci Function")
    if xhigh > 0:
        plt.plot(fibonnaci_real_pos, fibonnaci_imag_pos, 'o', label='Real Values')
    else:
        plt.plot(fibonnaci_real_neg, fibonnaci_imag_neg, 'o', label='Real Values')
    plt.axvline(x=0, c="black", linewidth=0.5)
    plt.axhline(y=0, c="black", linewidth=0.5)
    plt.title("Complex Fibonacci Sequence")
    plt.xlabel("Real(f_n)")
    plt.ylabel("Imag(f_n)")
    plt.legend()
    plt.show()
