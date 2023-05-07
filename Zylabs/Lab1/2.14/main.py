miles_per_gallon = float(input())
dollars_per_gallon = float(input())
   
dollars_20_miles  = 20  * (1.0 / miles_per_gallon) * dollars_per_gallon
dollars_75_miles  = 75  * (1.0 / miles_per_gallon) * dollars_per_gallon
dollars_500_miles = 500 * (1.0 / miles_per_gallon) * dollars_per_gallon

print(f'{dollars_20_miles:.2f} {dollars_75_miles:.2f} {dollars_500_miles:.2f}')
