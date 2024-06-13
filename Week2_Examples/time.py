class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours}:{self.minutes}'

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        return False

    def __sub__(self, other):
        time_diff = Time(0, 0)
        if self.minutes >= other.minutes:
            time_diff.minutes = self.minutes - other.minutes
            time_diff.hours = self.hours - other.hours
        else:
            time_diff.minutes = self.minutes - other.minutes + 60
            time_diff.hours = self.hours - other.hours - 1

        return time_diff
    # Class definition ends here

if __name__ == "__main__":

    # Note:  these are times on a 24-hour clock, on the same day
    time1 = Time(10, 45)
    time2 = Time(12, 15)
    time3 = Time(9, 45)

    print(f'Time1 = {time1}')
    print(f'Time2 = {time2}')
    print(f'Time3 = {time3}')

    min_time = time1  # Note:  Assignment operator works as expected by default!  No need to overload.
    if time2 < min_time:
        min_time = time2
    if time3 < min_time:
        min_time = time3

    print(f'The earliest time is {min_time}')

    if time1 == time3:
        print("Time1 and Time3 are the same!")
    else:
        print("Time1 and Time3 are not the same!")

    time4 = time2 - time1
    print(f'Time Difference (T2 - T1) = {time4}')

    time5 = time3 - time1
    print(f'Time Difference (T3 - T1) = {time5}')

    # __add__ method is not defined, so this will not work
    # __gt__ method is not defined, so this will not work
    # __ge__ method is not defined, so this will not work
    # __le__ method is not defined, so this will not work
    # __ne__ method is not defined, so this will not work
    # __mult__ method is not defined, so this will not work
    # __div__ method is not defined, so this will not work
