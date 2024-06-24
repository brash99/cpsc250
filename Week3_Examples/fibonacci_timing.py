def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":

    from timer import Timer

    #get help on the Timer class
    print(Timer.__doc__)
    # can also use 'help(Timer)' to get the same information

    timer = Timer()
    timer.start()

    nth_term = 29
    print(f"The {nth_term}th term of the Fibonacci sequence is {fibonacci(nth_term)}")

    elapsed = timer.stop()

    n = []
    elapsed_time = []
    fn = []
    for i in range(30):
        timer.start()
        fn.append(fibonacci(i))
        elapsed_time.append(timer.stop())
        n.append(i)

    print(n)
    print(fn)
    print(elapsed_time)

    import matplotlib.pyplot as plt
    plt.plot(n, elapsed_time)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity of Fibonacci Sequence')
    plt.show()