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
    # print(Timer.__doc__)
    # can also use 'help(Timer)' to get the same information

    timer = Timer()
    timer.start()

    nth_term = 29
    print(f"The {nth_term} term of the Fibonacci sequence is {fibonacci(nth_term)}")

    elapsed = timer.stop()

    # create some empty lists for plotting
    n = [] # x axis values
    elapsed_time = [] # y axis values

    fn = []

    for i in range(31):
        timer.start() # start the timer
        fnumber = fibonacci(i) # calculate the ith fibonacci number
        fn.append(fnumber) # append the ith fibonacci number to the list
        etime = timer.stop() # stop the timer and get the elapsed time
        elapsed_time.append(etime) # append the elapsed time to the list
        n.append(i) # append the value of i to the list

    print(n)
    print(fn)
    print(elapsed_time)

    import matplotlib.pyplot as plt
    plt.plot(n, elapsed_time)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.yscale('log')
    plt.grid()
    plt.yticks([0.000001,0.00001,0.0001, 0.001, 0.01, 0.1, 1], ['0.001ms','0.01ms','0.1ms','1ms', '10ms', '0.1s', '1s'])
    plt.title('Time Complexity of Calculating the Fibonacci Sequence using Recursion')
    plt.show()


    import math
    DeltaN = n[30]-n[10]
    DeltaT = math.log10(elapsed_time[30])-math.log10(elapsed_time[10])
    Slope = DeltaT/DeltaN
    print(f"Slope of the line is {Slope}")
    a = 10**Slope
    print(f"Time complexity of the Fibonacci sequence is O({a}^n) where n is the nth term of the sequence")