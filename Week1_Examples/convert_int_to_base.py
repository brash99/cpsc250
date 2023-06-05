num = 11
base = 4

num_original = num
res = ""

while num > 0:
    digit = num % base
    #print(num, digit)
    res = str(digit)+res
    num = int(num/base)

print(num_original, " = ", res, " in base ",base)
