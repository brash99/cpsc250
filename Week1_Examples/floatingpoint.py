import math

a = 0.1
b = 0.1
c = 0.1

# Here is a dangerous algorithm

print("Algorithm 1:")
print("a+b+c = ", a+b+c)

if a+b+c == 0.3:
    print("Sanity")
else:
    print("Insanity")

# Here is a better algorithm!
print("Algorithm 2:")
epsilon = 1.0E-10
expectedValue = 0.3

difference = (a+b+c) - expectedValue

if math.fabs(difference) < epsilon:
    print("Sanity")
else:
    print("Insanity")
