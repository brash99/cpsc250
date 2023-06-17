import decimal as dec
from timer import Timer
import matplotlib.pyplot as plt


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        t3 = 0
        for i in range(2, n+1):
            t3 = t2 + t1
            t1 = t2
            t2 = t3
        return t3


def fibonacci_phi(n):
    global phi
    global one, two, five, onehalf
    return round((phi**n-(-one/phi)**n)/five**onehalf)


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


if __name__ == "__main__":

    nmax = 40

    dec.getcontext().prec = 100

    one = dec.Decimal(1)
    two = dec.Decimal(2)
    five = dec.Decimal(5)
    onehalf = dec.Decimal(0.5)

    phi = (one + five ** onehalf) / two

    nplot = []
    nplotr = []
    tactual = []
    tformula = []
    trecursion = []

    for nth_term in range(nmax):

        nplot.append(nth_term)

        if nth_term % 10 == 0:
            ending = "th"
        elif nth_term % 10 == 1:
            ending = "st"
        elif nth_term % 10 == 2:
            ending = "nd"
        elif nth_term % 10 == 3:
            ending = "rd"
        else:
            ending = "th"

        time1 = Timer()
        time1.start()
        print(f"The Actual    {nth_term}{ending} term of the Fibonacci sequence is {fibonacci(nth_term)}")
        e1 = time1.stop()
        tactual.append(e1)

        print()

        time1.start()
        print(f"The Decimal   {nth_term}{ending} term of the Fibonacci sequence is {fibonacci_phi(nth_term)}")
        e2 = time1.stop()
        tformula.append(e2)

        print()

        if nth_term <= 30:
            nplotr.append(nth_term)
            time1.start()
            print(f"The Recursive {nth_term}{ending} term of the Fibonacci sequence is {fibonacci_recursive(nth_term)}")
            e3 = time1.stop()
            trecursion.append(e3)

    plt.plot(nplot, tactual)
    plt.plot(nplot, tformula)
    plt.plot(nplotr, trecursion)

    plt.title('Comparison of Different Algorithms for Fibonacci Number Calculation')
    plt.xlabel('Term of Fibonacci Sequence')
    plt.ylabel('Time (s)')
    plt.yscale('log')

    plt.show()
