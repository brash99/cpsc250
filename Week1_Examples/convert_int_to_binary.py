num = 11
num_original = num
res = ""

while num > 0:
    digit = num % 2
    #print(num, digit)
    res = str(digit)+res
    num = int(num/2)

print(num_original, " = ", res, " in binary.")
