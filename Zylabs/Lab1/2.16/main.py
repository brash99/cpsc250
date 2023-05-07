import math
x = float(input())
y = float(input())
z = float(input())
   
print(f'{math.pow(x, z):.2f} {math.pow(x, math.pow(y, z)):.2f} {math.fabs(x - y):.2f} {math.sqrt(math.pow(x, z)):.2f}')
