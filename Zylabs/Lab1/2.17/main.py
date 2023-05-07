import math

starting_frequency = int(input())
r = math.pow(2, (1 / 12))

print(f'{starting_frequency:.2f} Hz')
print(f'{starting_frequency * math.pow(r, 1):.2f} Hz')
print(f'{starting_frequency * math.pow(r, 2):.2f} Hz')
print(f'{starting_frequency * math.pow(r, 3):.2f} Hz')
