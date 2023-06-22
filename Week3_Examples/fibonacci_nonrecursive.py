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

    print(f"The {nth_term}{ending} term of the Fibonacci sequence is {fibonacci(nth_term)}")
