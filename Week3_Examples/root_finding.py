def f(x):
    return -4.0*x + 3.0


def find_root(a, b):
    epsilon = 1.0E-8
    fa = f(a)
    fb = f(b)
    print(a,b,fa,fb)
    if abs(fa-fb) < epsilon:
        print("Type 1: Found root at x = ", a)
    else:
        c = (a+b)/2.0
        fc = f(c)
        if fc == 0.0:
            print("Type 2: Found root at x = ", c)
        else:
            if fa*fc < 0.0:
                find_root(a, c)
            else:
                find_root(c, b)


if __name__ == "__main__":

    a = 0.0
    b = 5.0
    fa = f(a)
    fb = f(b)

    if fa*fb > 0:
        print(a,b,fa,fb)
        print("No root on this interval!!")
    elif fa*fb == 0:
        if fa == 0:
            print("Type 3a: Found root at x = ", a)
        else:
            print("Type 3b: Found root at x = ", b)
    else:
        find_root(a, b)
