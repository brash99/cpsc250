def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        for i in range(2, n+1):
            t3 = t2 + t1
            t1 = t2
            t2 = t3
        return t3


if __name__ == "__main__":

    nth_term = 1000

    print(f"The {nth_term} term of the Fibonacci sequence is {fibonacci(nth_term)}")
