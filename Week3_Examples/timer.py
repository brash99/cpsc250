# timer.py

import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:

    '''This class represents a timer object that can be used to
    measure the elapsed time of a code snippet

    Instantiation:
    timer1 = Timer()

    The timer object has the following methods:
    start(): This method starts the timer
    stop(): This method stops the timer and returns the elapsed time (in seconds, as a float)

    Usage:

    timer1 = Timer()
    timer1.start()

    .
    .
    . code snippet
    .
    .

    elapsed_time = timer1.stop()
    '''

    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return elapsed_time
