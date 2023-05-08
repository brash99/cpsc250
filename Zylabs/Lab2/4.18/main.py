is_leap_year = False
   
input_year = int(input())
   
if (input_year % 4) == 0:           # inputYear is divisible by 4
    if (input_year % 100) == 0:     # inputYear is divisible by 100 (century year)
        if (input_year % 400) == 0:  # inputYear is divisible by 400
            is_leap_year = True
        else:                      # inputYear is not divisible by 400
            is_leap_year = False
    else:                          # inputYear is not divisible by 100
        is_leap_year = True
else:                              # inputYear is not divisible by 4
    is_leap_year = False
   
if is_leap_year:
    print(f'{ input_year } - leap year')
else:
    print(f'{ input_year } - not a leap year')
