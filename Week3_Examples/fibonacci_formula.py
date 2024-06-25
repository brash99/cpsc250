import math
import decimal as dec


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
    return int((phi**n-(-1/phi)**n)/math.sqrt(5))


def fibonacci_phin(n):
    global phin
    global one, two, five, onehalf
    return round((phin**n-(-one/phin)**n)/five**onehalf)


if __name__ == "__main__":

    nth_term = 199

    dec.getcontext().prec = 100  # select 100 decimal place precision

    one = dec.Decimal(1)
    two = dec.Decimal(2)
    five = dec.Decimal(5)
    onehalf = dec.Decimal(0.5)

    phi = (1 + math.sqrt(5)) / 2

    phin = (one + five ** onehalf) / two

    #print(one)
    #print(two)
    #print(five)
    #print(onehalf)

    print(phi)
    print(phin)

    print(f"The actual       {nth_term} term of the Fibonacci sequence is {fibonacci(nth_term)}")
    print(f"The Python math  {nth_term} term of the Fibonacci sequence is {fibonacci_phi(nth_term)}")
    print()
    print(f"The Decimal math {nth_term} term of the Fibonacci sequence is {fibonacci_phin(nth_term)}")
