import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":

    nth_term = 25

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

    print(math.log10(300))
    print(math.log(300))