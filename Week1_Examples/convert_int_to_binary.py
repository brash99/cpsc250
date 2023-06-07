# Using built-in function
num = 11
b = bin(num)
print(num, " = ", b, " in binary.")

num_original = num
res = ""

while num > 0:
    digit = num % 2
    num = int(num/2)
    # print(num, digit)
    res = str(digit)+res


print(num_original, " = ", res, " in binary.")
