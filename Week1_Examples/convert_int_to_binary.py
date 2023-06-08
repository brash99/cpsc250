# Using built-in function
num = 4095
b = bin(num)
print(num, " = ", b, " in binary.")

num_original = num
result = ""

while num > 0:
    digit = num % 2
    num = int(num/2)
    # print(num, digit)
    result = str(digit)+result


print(num_original, " = ", result, " in binary.")
