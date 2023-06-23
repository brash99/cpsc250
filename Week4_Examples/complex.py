import cmath
import math

a = 4
b = 3
z = complex(a,b)

print(f'The real part of z is {z.real}')
print(f'The imaginary part of z is {z.imag}')

w = cmath.polar(z)

print(f'The size and phase of z are {w[0]} and {w[1]}, respectively.')

z2 = 5 + 3j

w2 = cmath.polar(0+1j)
print(f'The phase of w2 is {w2[1]*180.0/math.pi} degrees.')

z3 = cmath.rect(w2[0],w2[1])
print(f'The real and imaginary parts of w2 are {z3}')


